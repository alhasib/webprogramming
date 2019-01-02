from django.forms import ModelForm
from django import forms
from .models import *


# Create the form class.
class PlayerRegistrationForm(forms.ModelForm):
        class Meta:
            model = PlayerRegistration
            fields = '__all__' 


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  


class ClubRegistratoinForm(forms.ModelForm):
    class Meta:
        model = ClubRegistratoin
        fields = '__all__'                   


class PlayersPerformanceForm(forms.ModelForm):
    class Meta:
        model = PlayersPerformance
        fields = '__all__'      


class MatchInformationForm(forms.ModelForm):
    class Meta:
        model = MatchInformation
        fields = '__all__'      

class TeamInformationForm(forms.ModelForm):
    class Meta:
        model = TeamInformation
        fields = '__all__'      
          