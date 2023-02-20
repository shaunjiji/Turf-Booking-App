from django import forms
from .models import *
from django.forms.widgets import NumberInput



#Create a booking form

class BookingForm(forms.Form):
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'class': 'nice-select'}))
    time = forms.CharField(
        widget=forms.Select(choices=TIME_CHOICES, attrs={'class': 'nice-select'})
    )