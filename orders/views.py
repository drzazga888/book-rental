# -*- encoding: utf-8 -*-
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect

from books.models import Book, Categories
from orders.models import Order, OrderedBook
from users.models import Adress

from books.models import Book, Categories, Rates
from orders.models import OrderedBook
from books.forms import RatesForm
from contact.models import ContactData
from django.utils import timezone
import hashlib

def checkout(request):
    settings = ContactData.getFullConfig()
    address = Adress.objects.get(user_id=request.user.id)
    md5 = hashlib.md5()
    md5.update(str(timezone.now())+str(request.user.username))
    title = md5.hexdigest()
    template = loader.get_template('checkout.html')
    context = RequestContext(request, {'address':address, 'user':request.user, 'settings':settings, 'title':title})
    return HttpResponse(template.render(context))

def finalize(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            print request.POST.getlist("book[]")
            order = Order(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                          street=request.POST['street'], number=request.POST['number'], zip=request.POST['zip'], \
                          city=request.POST['city'], price=request.POST['summary'], withdrawtype=request.POST['collection'], \
                          user=request.user, paid=0, \
                          phone=request.POST['phone'], title=request.POST['title'])
            order.save()
            for book in request.POST.getlist("book[]"):
                tmpbook = Book.objects.get(id=book)
                orderedbook = OrderedBook(title=tmpbook.title, author=tmpbook.author, publisher=tmpbook.publisher, price=tmpbook.price, returned=0, book=tmpbook, order=order)
                orderedbook.save()
            request.session["message"] = u"Zamówienie zostało złożone. Zostanie zrealizowane niezwłocznie po zaksięgowaniu wpłaty"
            request.session["message_context"] = "success"
            return HttpResponseRedirect('/')
        else:
            request.session["message"] = u"Przed złożeniem zamówienia zaloguj się lub załóż konto"
            request.session["message_context"] = "danger"
            return HttpResponseRedirect('/users/authenticate')
    else:
        request.session["message"] = u"Zamówienie nie zostało wysłane poprawnie"
        request.session["message_context"] = "danger"
        return HttpResponseRedirect('/orders/checkout')

def loaned(request):
    if request.user.is_authenticated():
        orders = Order.objects.filter(user_id=request.user.id).order_by('date_order')
        books = []
        for order in orders:
            books += order.getBooks().filter(returned=0)
        print books[0].paid
        #books = OrderedBook.objects.all()
        template = loader.get_template('loaned.html')
        context = RequestContext(request, {'books': books})
        return HttpResponse(template.render(context))
    else:
        request.session["message"] = u"Zaloguj się, aby zobaczyć wypożyczone książki"
        request.session["message_context"] = "danger"
        return HttpResponseRedirect('/users/authenticate')
