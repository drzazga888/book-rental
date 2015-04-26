from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class NewUser(models.Model):
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Wymagane do 30 znakow, litery, cyfry oraz @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _("Wprowadz poprawna  nazwe uzytkownika. "
                                        "Ta wartosc moze zawierac tylko litery, cyfry oraz znaki @/./+/-/_"), 'invalid'),
        ],
        error_messages={
            'unique': _("Uzytkownik z ta nazwa juz istnieje."),
        })
    password = models.CharField(_('password'), max_length=128)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    street = models.CharField(_('street'), max_length=40)
    number = models.CharField(_('number of house'), max_length=6)
    zip = models.CharField(_('zip code'), max_length=6)
    city = models.CharField(_('city'), max_length=50)

class ResetPass(models.Model):
    key = models.CharField(_('key'), max_length=32, unique=True)
    user = models.OneToOneField(User, primary_key=True)
    date = models.DateTimeField(_('date created'), default=timezone.now)

class Adressess(models.Model):
    user = models.OneToOneField(User, primary_key=True, unique=True)
    street = models.CharField(_('street'), max_length=40)
    number = models.CharField(_('number of house'), max_length=6)
    zip = models.CharField(_('zip code'), max_length=6)
    city = models.CharField(_('city'), max_length=50)