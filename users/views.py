# -*- encoding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
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


def authenticate(request):
    template = loader.get_template('auth.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
   

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=str(form.cleaned_data['username']).replace('@', '_'), password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('authenticate')
    else:
        return HttpResponseRedirect("authenticate")

def logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def register(request):
    if request.method == 'POST':
        post = request.POST.copy()
        md5 = hashlib.md5()
        md5.update(str(timezone.now())+str(request.POST['username']))
        post['userkey'] = md5.hexdigest()
        tmpuser = User()
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
            return HttpResponseRedirect("/")
        else:
            print form.errors
            return HttpResponseRedirect('authenticate')
    else:
        return HttpResponseRedirect("authenticate")

def confirm(request, user, key):
    print "makarena-3"
    username = urllib.unquote_plus(user)
    print "makarena-2"
    reguser = NewUser.objects.filter(username__contains=username).filter(userkey__contains=key)
    print "makarena-1:", "len =", len(reguser), ",username =", username, ",key =", key, "; eeeeee makarena"
    if len(reguser) == 1:
        print "makarena0"
        user = User.objects.create_user(str(reguser[0].username).replace('@', '_'), reguser[0].username, 'tmp')
        print "makarena1"
        user.password = reguser[0].password
        print "makarena2"
        user.save()
        print "makarena3"
        address = Adress(id=user.id, street=reguser[0].street, number=reguser[0].number,
                         zip=reguser[0].zip, city=reguser[0].city, )
        print "makarena4"
        address.save()
        print "makarena5"
        return HttpResponseRedirect("authenticate")
    else:
        return HttpResponseRedirect("/")

# pomocnicza funkcja
def build_mail(form):
    message = u'<!DOCTYPE html><html><head><meta charset="utf-8" /><title>Email</title></head><body>Witaj <b>' + form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name'] \
        + u"</b><br />Aby potwierdzić rejestrację kliknij w poniższy link:<br />" \
        + u'<a href="http://'+APP_HOST+'/users/confirm/user/' +urllib.quote_plus(form.cleaned_data['username']) \
        + u'/key/' + form.cleaned_data['userkey'] + u'">POTWIERDŹ</a><br/><br />Pozdrawiam<br />Administrator</body></html>'
    return message

