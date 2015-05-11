# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate as django_auth
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import LoginForm, RegisterForm
from users.models import NewUser, Adress
from django.template import RequestContext, loader
from django.utils import timezone
import hashlib
import urllib
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from library.settings import EMAIL_HOST_USER, APP_HOST


"""
***********************************************
* KOMUNIKATY OD STRONY SERWERA DO UŻYTKOWNIKA *
***********************************************

Ustawiam do słownika sesji (request.session) 2 wartości:
- message - wiadomość do wypisania dla użytkownika
- message_context - kontekst, wydźwięk wiadomości,
    tak naprawdę jest to klasa, która jest ustawiana
    odpowiedniemu elementowi w szablonie, od bootstrapa mamy np:
    - success
    - info
    - warning
    - danger
    więcej info na: http://getbootstrap.com/css/#helper-classes-backgrounds

Przykład:
    request.session["message"] = u"Logowanie przebiegło pomyślnie!"
    request.session["message_context"] = "success"

Po wyświetleniu wiadomości naleźy usunąć te wiadomości z sesji,
robimy to tak:
    del request.session["message"]
    del request.session["message_context"]

"""


def authenticate(request):
    template = loader.get_template('auth.html')
    context = RequestContext(request, {})
    render_result = template.render(context)
    if "message" in request.session:
        del request.session["message"]
    if "message_context" in request.session:
        del request.session["message_context"]
    return HttpResponse(render_result)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = str(form.cleaned_data['username']).replace('@', '_')
            password = form.cleaned_data['password']
            user = django_auth(username=username, password=password)
            if user is not None:
                django_login(request, user)
                request.session["message"] = u"Logowanie przebiegło pomyślnie!"
                request.session["message_context"] = "success"
                #return HttpResponseRedirect('/')
                return HttpResponseRedirect('/users/authenticate')
    request.session["message"] = u"Błąd logowania. Spróbuj jeszcze raz."
    request.session["message_context"] = "danger"
    return HttpResponseRedirect("authenticate")


def logout(request):
    django_logout(request)
    request.session["message"] = u"Wylogowano pomyślnie!"
    request.session["message_context"] = "info"
    #return HttpResponseRedirect("/")
    return HttpResponseRedirect('/users/authenticate')


def register(request):
    if request.method == 'POST':
        post = request.POST.copy()
        md5 = hashlib.md5()
        md5.update(str(timezone.now())+str(request.POST['username']))
        post['userkey'] = md5.hexdigest()
        tmpuser = User()
        #walidacja hasla
        get_pass = post['password']
        valid_pass = post['password2']
        if get_pass != valid_pass:
            request.session["message"] = u"Podane hasła nie są identyczne!"
            request.session["message_context"] = "danger"
            return HttpResponseRedirect("/users/authenticate")
        tmpuser.set_password(post['password'])
        post['password'] = tmpuser.password
        form = RegisterForm(post)
        if form.is_valid():
            form.save()
            email = EmailMessage('Potwierdzenie rejestracji', build_mail(form), EMAIL_HOST_USER,
                [form.cleaned_data['username']], reply_to=[EMAIL_HOST_USER],
                headers={'Content-Type': 'text/html', 'Message-ID': 'register'})
            email.content_subtype = "html"
            email.encoding = 'utf8'
            email.send()
            request.session["message"] = u"W celu ukończenia rejestracji prosimy sprawdzić konto e-mail w poszukiwaniu wiadomości potwierdzającej."
            request.session["message_context"] = "info"
            #return HttpResponseRedirect('/users/authenticate')
            return HttpResponseRedirect("/")
        else:
            print form.errors
    request.session["message"] = u"Błąd rejestracji. Spróbuj ponownie."
    request.session["message_context"] = "danger"
    return HttpResponseRedirect("/users/authenticate")


def confirm(request, user, key):
    username = urllib.unquote_plus(user)
    reguser = NewUser.objects.filter(username__contains=username).filter(userkey__contains=key)
    if len(reguser) == 1:
        user = User.objects.create_user(str(reguser[0].username).replace('@', '_'), reguser[0].username, 'tmp')
        user.password = reguser[0].password
        user.save()
        address = Adress(user=user, street=reguser[0].street, number=reguser[0].number, zip=reguser[0].zip, city=reguser[0].city,)
        address.save()
        request.session["message"] = u"Rejestracja ukończona pomyślnie. Możesz się już zalogować."
        request.session["message_context"] = "success"
        return HttpResponseRedirect("/users/authenticate")
    request.session["message"] = u"Błędne zatwierdzanie e-maila"
    request.session["message_context"] = "danger"
    #return HttpResponseRedirect("/")
    return HttpResponseRedirect("/users/authenticate")


# pomocnicza funkcja
def build_mail(form):
    message = u'<!DOCTYPE html><html><head><meta charset="utf-8" /><title>Email</title></head><body>Witaj <b>' + form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name'] \
        + u"</b><br />Aby potwierdzić rejestrację kliknij w poniższy link:<br />" \
        + u'<a href="http://'+APP_HOST+'/users/confirm/user/' +urllib.quote_plus(form.cleaned_data['username']) \
        + u'/key/' + form.cleaned_data['userkey'] + u'">POTWIERDŹ</a><br/><br />Pozdrawiam<br />Administrator</body></html>'
    return message
