from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book, Categories
from orders.models import Order, OrderedBook

def checkout(request):
    template = loader.get_template('checkout.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def finalize(request):
    return HttpResponseRedirect('/')

def loaned(request):
    orders = Order.objects.filter(user_id=request.user.id)
    books = []
    for order in orders:
        books += order.getBooks().filter(returned=0)
    print books
    return HttpResponse("Tutaj beda juz wypozyczone ksiazki")