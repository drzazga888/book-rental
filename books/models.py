from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Categories(models.Model):
    name = models.CharField(_('name of category'), max_length=40)

class Book(models.Model):
    category = models.ForeignKey(Categories, _('category'))
    title = models.CharField(_('title of book'), max_length=70)
    description = models.TextField(_('ddescription'))
    author = models.CharField(_('author'), max_length=60)
    publisher = models.CharField(_('publisher'), max_length=60)
    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2)
    quantity = models.IntegerField(_('quantity of books'), default=1)
    date_added = models.DateTimeField(_('date added'), default=timezone.now)
    sale = models.BooleanField(_('sale'), blank=False)