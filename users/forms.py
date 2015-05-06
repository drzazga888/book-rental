# -*- encoding: utf-8 -*-
from django import forms
from users.models import NewUser
from django.utils.translation import ugettext_lazy as _

class RegisterForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ['username', 'password', 'first_name', 'last_name', 'street', 'number', 'zip', 'city', 'userkey']

    username = forms.EmailField(label=_('username'), required=True)
    password = forms.CharField(label=_('password'), max_length=128, required=True)
    first_name = forms.CharField(label=_('first name'), max_length=30, required=True)
    last_name = forms.CharField(label=_('last name'), max_length=30, required=True)
    street = forms.CharField(label=_('street'), max_length=40, required=True)
    number = forms.CharField(label=_('number of house'), max_length=7, required=True)
    zip = forms.CharField(label=_('zip code'), max_length=6, required=True)
    city = forms.CharField(label=_('city'), max_length=50, required=True)
    userkey = forms.CharField(label=_('key'), max_length=32, required=True)

class LoginForm(forms.Form):
    username = forms.EmailField(label=_('username'), required=True)
    password = forms.CharField(label=_('password'), max_length=60, required=True)