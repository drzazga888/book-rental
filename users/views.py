# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate as django_auth
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import LoginForm, RegisterForm
from users.models import NewUser, Adress, ResetPass
from django.template import RequestContext, loader
from django.utils import timezone
import hashlib
import urllib
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from library.settings import EMAIL_HOST_USER, APP_HOST
from newsletter.models import Newsletter


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
    context = RequestContext(request, {'title':'Logowanie / Rejestracja'})
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
                return HttpResponseRedirect('/')
    request.session["message"] = u"Błąd logowania. Spróbuj jeszcze raz."
    request.session["message_context"] = "danger"
    return HttpResponseRedirect("authenticate")


def logout(request):
    django_logout(request)
    request.session["message"] = u"Wylogowano pomyślnie!"
    request.session["message_context"] = "info"
    return HttpResponseRedirect("authenticate")


def register(request):
    if request.method == 'POST':
        post = request.POST.copy()
        md5 = hashlib.md5()
        md5.update(str(timezone.now())+str(request.POST['username']))
        post['userkey'] = md5.hexdigest()
        tmpuser = User()
        # walidacja hasla
        get_pass = post['password']
        valid_pass = post['password2']
        if get_pass != valid_pass:
            request.session["message"] = u"Podane hasła nie są identyczne!"
            request.session["message_context"] = "danger"
            return HttpResponseRedirect("authenticate")
        tmpuser.set_password(post['password'])
        post['password'] = tmpuser.password
        form = RegisterForm(post)
        if form.is_valid():
            form.save()
            email = EmailMessage('Potwierdzenie rejestracji', build_mail_confirm(form), EMAIL_HOST_USER,
                [form.cleaned_data['username']], reply_to=[EMAIL_HOST_USER],
                headers={'Content-Type': 'text/html', 'Message-ID': 'register'})
            email.content_subtype = "html"
            email.encoding = 'utf8'
            email.send()
            request.session["message"] = u"W celu ukończenia rejestracji prosimy sprawdzić konto e-mail w poszukiwaniu wiadomości potwierdzającej."
            request.session["message_context"] = "info"
            return HttpResponseRedirect("authenticate")
        else:
            print form.errors
    request.session["message"] = u"Błąd rejestracji. Spróbuj ponownie."
    request.session["message_context"] = "danger"
    return HttpResponseRedirect("authenticate")


def confirm(request, user, key):
    username = urllib.unquote_plus(user)
    reguser = NewUser.objects.filter(username=username).filter(userkey=key)
    if len(reguser) == 1:
        user = User.objects.create_user(str(reguser[0].username).replace('@', '_'), reguser[0].username, 'tmp')
        user.password = reguser[0].password
        user.save()
        address = Adress(user=user, street=reguser[0].street, number=reguser[0].number, zip=reguser[0].zip, city=reguser[0].city,)
        address.save()
        if Newsletter.objects.filter(email=reguser[0].username) is None:
            newsletter = Newsletter(email=reguser[0].username)
            newsletter.save()
        reguser.delete()
        request.session["message"] = u"Rejestracja ukończona pomyślnie. Możesz się już zalogować."
        request.session["message_context"] = "success"
        return HttpResponseRedirect("authenticate")
    request.session["message"] = u"Błędne zatwierdzanie e-maila"
    request.session["message_context"] = "danger"
    return HttpResponseRedirect("authenticate")


def remind(request):
    print ">wywolano funkcje remind"
    email = request.POST['email']
    new_pass = request.POST['password']
    valid_pass = request.POST['password2']
    print ">>pobrano dane (POST)"
    #sprawdzanie poprawnosci hasel
    if new_pass != valid_pass:
        request.session["message"] = u"Podane hasła nie są identyczne!"
        request.session["message_context"] = "danger"
        return HttpResponseRedirect("authenticate")
    print ">>sprawdzono poprawnosc hasel"
    user = User.objects.filter(email=email)
    if user.exists():
        print ">>(i)uzytkownik istnieje w bazie"
        user = user[0]
        #generowanie key'a
        md5 = hashlib.md5()
        md5.update(str(timezone.now())+str(user.username))
        key = md5.hexdigest()
        print ">>wygenerowano nowe haslo i key"
        #wstawienie danych do bazy
        passwd = User()
        passwd.set_password(new_pass)
        resetpass = ResetPass(key=key, user_id=user.id, date=timezone.now(), password=passwd.password)
        resetpass.save()
        print ">>utworzono dane tymczasowe"
        #wyslanie mail'a
        email = EmailMessage('Nowo wygenerowane hasło', build_mail_reminder(user, new_pass, key), EMAIL_HOST_USER,
                [user.email], reply_to=[EMAIL_HOST_USER],
                headers={'Content-Type': 'text/html', 'Message-ID': 'register'})
        email.content_subtype = "html"
        email.encoding = 'utf8'
        email.send()
        print ">>wyslano emaila"
    return HttpResponseRedirect("authenticate")

def reset(request, user, key):
    print ">wywolano funkcji reset"
    username = urllib.unquote_plus(user).replace('@', '_')
    print ">>(i)pobrano nazwe uzytkownika: ", username
    user_pass = User.objects.filter(username=username)
    print ">>(i)znaleziono", len(user_pass), "pasujacych uzytkownikow w bazie"
    if len(user_pass) == 1:
        print ">>(i)user id =", user_pass[0].id
        reset_pass = ResetPass.objects.filter(user=user_pass[0].id).filter(key=key)
        print ">>(i)znaleziono ", len(reset_pass), "pasujacych uzytkownikow w tymczasowej tablicy bazy danych"
        print ">>wyfiltrowano odpowiednie rekordy w bazach"
        if len(reset_pass) == 1:
            print ">>znaleziono unikatowe rekordy"
            user_pass[0].password = reset_pass[0].password
            user_pass[0].save()
            print ">>zmieniono haslo w bazie"
            reset_pass[0].delete()
            print ">>usunieto dane tymczasowe w bazie"
            request.session["message"] = u"Hasło zostało zresetowane. Zaloguj się z hasłem podanym w email'u."
            request.session["message_context"] = "success"
            return HttpResponseRedirect("authenticate")
    print ">>(!)nie znaleziono unikatowych rekordow"
    request.session["message"] = u"Błędne zatwierdzanie e-maila"
    request.session["message_context"] = "danger"
    return HttpResponseRedirect("authenticate")



# pomocnicza funkcja
def build_mail_confirm(form):
    comfirmation_address = u'http://'+APP_HOST+u'/users/confirm/user/' +urllib.quote_plus(form.cleaned_data['username'])+ u'/key/' + form.cleaned_data['userkey']
    message = (
        u'<!DOCTYPE html>'
        u'<html>'
        u'<head>'
            u'<meta charset="utf-8" />'
            u'<title>Email</title>'
        u'</head>'
        u'<body>'
            u'<h2>Witaj ' + form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name'] + u'</h2>'
            u'<p>'
                u'Aby potwierdzić rejestrację kliknij w poniższy link:<br />'
                u'<a href="'+comfirmation_address+ u'">'+comfirmation_address+ u'</a>'
            u'</p>'
            u'<p>'
                u'Pozdrawiam<br />'
                u'Administrator'
            u'</p>'
        u'</body>'
        u'</html>'
    )
    return message

def build_mail_reminder(user, password, key):
    reseting_address = u'http://'+APP_HOST+u'/users/reset/user/' +urllib.quote_plus(user.email)+ u'/key/' + key
    message = (
        u'<!DOCTYPE html>'
        u'<html>'
        u'<head>'
            u'<meta charset="utf-8" />'
            u'<title>Email</title>'
        u'</head>'
        u'<body>'
            u'<h2>Witaj</h2>'
            u'<p>Twoje nowe hasło to: '+password+ u'</p>'
            u'<p>'
                u'Kliknij by zatwierdzić zmiane hasła.<br />'
                u'<a href="'+reseting_address+ u'">'+reseting_address+ u'</a>'
            u'</p>'
            u'<p>'
                u'Pozdrawiam<br />'
                u'Administrator'
            u'</p>'
        u'</body>'
        u'</html>'
    )
    return message