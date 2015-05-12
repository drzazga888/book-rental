from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book, Categories, Rates
from books.forms import RatesForm
from contact.models import OpeningHours, ContactData
from django.core.mail import EmailMessage


def index(request):
    hours = OpeningHours.objects.all()
    settings = ContactData.getFullConfig()
    template = loader.get_template('contact.html')
    context = RequestContext(request, {'hours':hours, 'settings':settings})
    return HttpResponse(template.render(context))

def sendmail(request):
    settings = ContactData.getFullConfig()
    email = EmailMessage(request.POST['subject']+' FROM: '+request.POST['name'], request.POST['message'], settings['email'],
            reply_to=request.POST['email'], headers={'Content-Type': 'text/html', 'Message-ID': 'contact'})
    #email.content_subtype = "html"
    email.encoding = 'utf8'
    email.send()
    return HttpResponseRedirect('/')