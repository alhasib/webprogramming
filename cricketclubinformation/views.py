from django.shortcuts import render
from .forms import *

def player_registration(request):
    # form = PlayerRegistrationForm()
    # context = {'form':form}
    return render(request, 'player_registration.html')