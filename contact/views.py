from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book, Categories, Rates
from books.forms import RatesForm

def index(request):
    template = loader.get_template('contact.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def sendmail(request):
    return HttpResponseRedirect('/')