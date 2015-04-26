from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Newsletter(models.Model):
    email = models.CharField(_('e-mail'), max_length=30, unique=True,
        help_text=_('Wymagane do 30 znakow, litery, cyfry oraz @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@]+$',
                                      _("Wprowadz poprawny adres e-mail. "
                                        "Ta wartosc moze zawierac tylko litery, cyfry oraz znak @."), 'invalid'),
        ],
        error_messages={
            'unique': _("Podany adres e-mail juz istnieje  w bazie."),
        })