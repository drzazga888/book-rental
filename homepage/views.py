from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Categories, Book
from homepage.models import Slider, NewBooks, TopLoaned, TopRates

# Create your views here.
def index(request):
    # categories
    categories = Categories.objects.order_by('name')
    # slider
    slider = Slider.objects.order_by('sequence')
    #top rates
    toprates = TopRates.objects.all()
    #new books
    newbooks = NewBooks.objects.all()
    #top loaned
    toploaned = TopLoaned.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {'categories':categories, 'slider':slider, 'toprates':toprates, \
                                       'newbooks':newbooks, 'toploaned':toploaned})
    return HttpResponse(template.render(context))