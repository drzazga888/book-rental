# -*- encoding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from newsletter.models import Newsletter

# Create your views here.

def add(request):
    if Newsletter.objects.filter(email=request.POST['email']) != None:
        newsletter = Newsletter(email=request.POST['email'])
        newsletter.save()
        request.session["message"] = u"Zostałeś zapisany do newsletter'a"
        request.session["message_context"] = "success"
    else:
        request.session["message"] = u"Podany adres już istnieje w bazie"
        request.session["message_context"] = "danger"
    return HttpResponseRedirect('/')