from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, _('user'))
    date_order = models.DateTimeField(_('date order'), default=timezone.now)
    total_price = models.DecimalField(_('total price'), max_digits=5, decimal_places=2)
    paid = models.BooleanField(_('paid'), blank=False)
    realized = models.BooleanField(_('realized'), blank=False)

class OrderedBook(models.Model):
    order = models.ForeignKey(Order, _('order'))
    title = models.CharField(_('title of book'), max_length=70)
    author = models.CharField(_('author'), max_length=60)
    publisher = models.CharField(_('publisher'), max_length=60)
    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2)
    book = models.ForeignKey(Book, _('book'))
    returned = models.BooleanField(_('returned'), blank=False)