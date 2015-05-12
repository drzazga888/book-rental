from django.db import models
from django.utils.translation import ugettext_lazy as _

class OpeningHours(models.Model):
    day = models.CharField(verbose_name=_('day'), max_length=70)
    open = models.TimeField(verbose_name=_('open hour'))
    close = models.TimeField(verbose_name=_('close hour'))

class ContactData(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=70)
    value = models.CharField(verbose_name=_('value'), max_length=70)

    @staticmethod
    def getFullConfig():
        tmp_settings = ContactData.objects.all()
        settings = {}
        for tmp in tmp_settings:
            settings[tmp.name] = tmp.value
        return settings