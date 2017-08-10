# forms.py
from django.forms import ModelForm, ValidationError
from django import forms
from django.contrib import messages

from .models import Subscriber



class CreateSubscriberForm(ModelForm):

    def clean(self):
        cleaned_data = super(CreateSubscriberForm, self).clean()
        return cleaned_data

    class Meta:
        model = Subscriber
        fields = ['email', 'first_name', 'last_name', 'country', 'state', 'occupation' , 'language_speak', 'language_teach', 'notifications_on' ]
        widgets = {
        	'country': forms.Select(),
        	'state': forms.Select(),
        	'occupation': forms.Select(),
        	'language_speak': forms.SelectMultiple(),
        	'language_teach': forms.SelectMultiple()
        }