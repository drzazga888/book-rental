# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), to_field='id')
    first_name = models.CharField(verbose_name=_('first name'), max_length=30)
    last_name = models.CharField(verbose_name=_('last name'), max_length=30)
    date_order = models.DateTimeField(verbose_name=_('date order'), default=timezone.now)
    street = models.CharField(verbose_name=_('street'), max_length=40)
    number = models.CharField(verbose_name=_('number of house'), max_length=8)
    zip = models.CharField(verbose_name=_('zip code'), max_length=6)
    city = models.CharField(verbose_name=_('city'), max_length=50)
    price = models.DecimalField(verbose_name=_('price'), max_digits=5, decimal_places=2)
    withdrawtype = models.CharField(verbose_name=_('withdraw type'), max_length=50)
    paid = models.BooleanField(verbose_name=_('paid'), blank=False, default=0)

    def getBooks(self):
        return OrderedBook.objects.filter(order=self)

class OrderedBook(models.Model):
    title = models.CharField(verbose_name=_('title of book'), max_length=70)
    author = models.CharField(verbose_name=_('author'), max_length=60)
    publisher = models.CharField(verbose_name=_('publisher'), max_length=60)
    price = models.DecimalField(verbose_name=_('price'), max_digits=5, decimal_places=2)
    book = models.ForeignKey(Book, verbose_name=_('book'), to_field='id')
    returned = models.BooleanField(verbose_name=_('returned'), blank=False)
    order = models.ForeignKey(Order, verbose_name=_('order'), to_field='id')
