from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import LoginForm, RegisterForm
from users.models import NewUser
from django.template import RequestContext, loader
from django.shortcuts import render

def authenticate(request):
    template = loader.get_template('auth.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
   

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
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
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = NewUser(form)
            user.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('users/authenticate')
    else:
        return HttpResponseRedirect("users/authenticate")

"""#jak mam testowac funkcje
#jak mam uzywac zmiennych 'z formularzy'
#skad mam wiedziec jak wyglada baza
#z czym mam porownac email"""
