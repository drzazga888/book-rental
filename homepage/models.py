from django.db import models
from books.models import Book
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Slider(models.Model):
    book = models.OneToOneField(Book, _('book'), primary_key=True, unique=True)
    sequence = models.IntegerField(_('sequence'), unique=True)

class NewBooks(models.Model):
    book = models.OneToOneField(Book, _('book'), primary_key=True, unique=True)

class TopRates(models.Model):
    book = models.OneToOneField(Book, _('book'), primary_key=True, unique=True)

class TopLoaned(models.Model):
    book = models.OneToOneField(Book, _('book'), primary_key=True, unique=True)