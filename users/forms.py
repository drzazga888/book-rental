from django import forms
from django.utils.translation import ugettext_lazy as _

class RegisterForm(forms.Form):
    username = forms.EmailField(label=_('username'), required=False)
    password = forms.CharField(label=_('password'), max_length=60, required=False)
    first_name = forms.CharField(label=_('first name'), max_length=30, required=False)
    last_name = forms.CharField(label=_('last name'), max_length=30, required=False)
    date_joined = forms.DateTimeField(label=_('date joined'), required=False)
    street = forms.CharField(label=_('street'), max_length=40, required=False)
    number = forms.CharField(label=_('number of house'), max_length=6, required=False)
    zip = forms.CharField(label=_('zip code'), max_length=6, required=False)
    city = forms.CharField(label=_('city'), max_length=50, required=False)

class LoginForm(forms.Form):
    username = forms.EmailField(label=_('username'), required=False)
    password = forms.CharField(label=_('password'), max_length=60, required=False)