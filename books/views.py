# -*- encoding: utf-8 -*-
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book, Categories, Rates
from books.forms import RatesForm
from books.paginator import Paginator

def book(request, book_id):
    # categories
    categories = Categories.objects.order_by('name')
    book = Book.objects.get(id=book_id)
    rates= Rates.objects.filter(book_id=book_id)
    book.rates_length = len(rates)
    rate = 0
    for onerate in rates:
        rate+=onerate.rate
    if book.rates_length != 0:
        book.rate = rate/book.rates_length
    else:
        book.rate=0
    template = loader.get_template('book.html')
    context = RequestContext(request, {'book':book, 'rates':rates, 'categories':categories})
    return HttpResponse(template.render(context))

def comment(request, book_id):
    post = request.POST.copy()
    post['user'] = 1 # DO ZMIANY
    post['book'] = book_id
    post['rate'] = 4
    form = RatesForm(post)
    if form.is_valid():
        form.save()
    else:
        print form.errors
    return HttpResponseRedirect('/books/book/'+book_id)

def category(request, cat, page):
    # categories
    categories = Categories.objects.order_by('name')
    #category
    category = Categories.objects.get(id=cat)
    result_title = "Kategoria: " + category.name
    #books
    books = Book.objects.filter(category=cat)
    for book in books:
        book.description = book.description[:200] + '...'
    #paginator
    if not request.session.get('booksPerPage', None):
        request.session['booksPerPage'] = 20
    paginator = Paginator(site=page, length=len(books), perpage=request.session['booksPerPage'])
    template = loader.get_template('list.html')
    if paginator.start != 0:
        books = books[paginator.start-1:paginator.to]
    else:
        books = books[paginator.start:paginator.to]
    context = RequestContext(request, {'categories':categories, 'result_title':result_title, 'books':books, 'paginator':paginator})
    return HttpResponse(template.render(context))

def category_firstpage(request, cat):
    return category(request, cat, 1)

def perpage(request, length):
    request.session['booksPerPage'] = length
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def search(request, page):
    #init vars
    if request.POST['target'] != None:
        request.session['searchTarget'] = request.POST['target']
    if request.POST['query'] != None:
        request.session['searchQuery'] = request.POST['query']
    # categories
    categories = Categories.objects.order_by('name')
    #results
    target = request.session['searchTarget']
    query = request.session['searchQuery']
    if target == 'author':
        description = "Autor: "
        books = Book.objects.filter(author__contains=query)
    elif target == 'title':
        description = u'Tytuł: '
        books = Book.objects.filter(title__contains=query)
    elif target == 'description':
        description = "Opis: "
        books = Book.objects.filter(description__contains=query)
    else:
        books = Book.objects.all()
    #paginator
    if not request.session.get('booksPerPage', None):
        request.session['booksPerPage'] = 20
    paginator = Paginator(site=page, length=len(books), perpage=request.session['booksPerPage'])
    template = loader.get_template('list.html')
    if paginator.start != 0:
        books = books[paginator.start-1:paginator.to]
    else:
        books = books[paginator.start:paginator.to]
    result_title = description + query
    context = RequestContext(request, {'categories':categories, 'result_title':result_title, 'books':books, 'paginator':paginator})
    return HttpResponse(template.render(context))

def search_firstpage(request):
    return search(request, 1)