# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class OrderedBook(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), to_field='id')
    title = models.CharField(verbose_name=_('title of book'), max_length=70)
    author = models.CharField(verbose_name=_('author'), max_length=60)
    publisher = models.CharField(verbose_name=_('publisher'), max_length=60)
    price = models.DecimalField(verbose_name=_('price'), max_digits=5, decimal_places=2)
    date_order = models.DateTimeField(verbose_name=_('date order'), default=timezone.now)
    book = models.ForeignKey(Book, verbose_name=_('book'), to_field='id')
    paid = models.BooleanField(verbose_name=_('paid'), blank=False, default=0)
    returned = models.BooleanField(verbose_name=_('returned'), blank=False)
