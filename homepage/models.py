from django.db import models
from books.models import Book
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Slider(models.Model):
    book = models.OneToOneField(Book, verbose_name=_('book'), primary_key=True, unique=True, to_field='id')
    sequence = models.IntegerField(verbose_name=_('sequence'), unique=True)

class NewBooks(models.Model):
    book = models.OneToOneField(Book, verbose_name=_('book'), primary_key=True, unique=True, to_field='id')

class TopRates(models.Model):
    book = models.OneToOneField(Book, verbose_name=_('book'), primary_key=True, unique=True, to_field='id')

class TopLoaned(models.Model):
    book = models.OneToOneField(Book, verbose_name=_('book'), primary_key=True, unique=True, to_field='id')