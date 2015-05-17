from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book, Categories, Rates
from orders.models import OrderedBook
from books.forms import RatesForm

def checkout(request):
    template = loader.get_template('checkout.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def finalize(request):
    return HttpResponseRedirect('/')

def loaned(request):
    books = OrderedBook.objects.order_by('date_order')
    template = loader.get_template('loaned.html')
    context = RequestContext(request, {'books': books})
    return HttpResponse(template.render(context))