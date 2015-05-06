from django.forms import ModelForm
from books.models import Rates

class RatesForm(ModelForm):
    class Meta:
        model = Rates
        fields = ['rate', 'comment', 'user', 'book']