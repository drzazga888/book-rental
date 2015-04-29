from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Categories(models.Model):
    name = models.CharField(verbose_name=_('name of category'), max_length=40)

class Book(models.Model):
    category = models.ForeignKey(Categories, verbose_name=_('category'), to_field='id')
    title = models.CharField(verbose_name=_('title of book'), max_length=70)
    description = models.TextField(verbose_name=_('ddescription'))
    author = models.CharField(verbose_name=_('author'), max_length=60)
    publisher = models.CharField(verbose_name=_('publisher'), max_length=60)
    price = models.DecimalField(verbose_name=_('price'), max_digits=5, decimal_places=2)
    quantity = models.IntegerField(verbose_name=_('quantity of books'), default=1)
    date_added = models.DateTimeField(verbose_name=_('date added'), default=timezone.now)
    sale = models.BooleanField(verbose_name=_('sale'), blank=False)