from django.forms import ModelForm
from django import forms
from .models import *


# Create the form class.
class PlayerRegistrationForm(forms.ModelForm):
        class Meta:
            model = PlayerRegistration
            fields = '__all__' 