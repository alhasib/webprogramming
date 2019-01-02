from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

def home(request):
        return render(request, 'home.html')

def player_registration(request):
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            player = PlayerRegistration.objects.get(first_name = first_name)
            context = {'player':player}
            return render(request, 'player.html', context)

    form = PlayerRegistrationForm()
    context = {'form':form}
    return render(request, 'player_registration.html', context)



def contact(request):
        print('jj')
        if request.method == 'POST':
                print('jtt')
                form = ContactForm(request.POST)
                print('j')
                if form.is_valid():
                        print('jjp')
                        form.save()
                        club_id = form.cleaned_data['club_id']
                        contact_info = Contact.objects.get(club_id = club_id)
                        context = {'contact_info':contact_info}
                        return render(request, 'contact_info.html', context)
        form = ContactForm()
        context = {'form':form}
        return render(request, 'contact_form.html', context)


def club_registration(request):
        print('jj')
        if request.method == 'POST':
                print('jtt')
                form = ClubRegistratoinForm(request.POST)
                print('j')
                if form.is_valid():
                        print('jjp')
                        form.save()
                        club_name = form.cleaned_data['club_name']
                        club = ClubRegistratoin.objects.get(club_name = club_name)
                        context = {'club':club}
                        return render(request, 'club_info.html', context)
        form = ClubRegistratoinForm()
        context = {'form':form}
        return render(request, 'club_registration_form.html', context)


def player_performance(request):
        print('jj')
        if request.method == 'POST':
                print('jtt')
                form = PlayersPerformanceForm(request.POST)
                print('j')
                if form.is_valid():
                        print('jjp')
                        form.save()
                        match_id = form.cleaned_data['match_id']
                        performance = PlayersPerformance.objects.get(match_id = match_id)
                        context = {'performance':performance}
                        return render(request, 'performance_info.html', context)
        form = PlayersPerformanceForm()
        context = {'form':form}
        return render(request, 'performance_form.html', context) 


def match_information(request):
        print('jj')
        if request.method == 'POST':
                print('jtt')
                form = MatchInformationForm(request.POST)
                print('j')
                if form.is_valid():
                        print('jjp')
                        form.save()
                        event_id = form.cleaned_data['event_id']
                        match_info = MatchInformation.objects.get(event_id = event_id)
                        context = {'match_info':match_info}
                        return render(request, 'match_info.html', context)
        form = MatchInformationForm()
        context = {'form':form}
        return render(request, 'match_information_form.html', context)         

def team_information(request):
        print('jj')
        if request.method == 'POST':
                print('jtt')
                form = TeamInformationForm(request.POST)
                print('j')
                if form.is_valid():
                        print('jjp')
                        form.save()
                        club_id = form.cleaned_data['club_id']
                        team_info = TeamInformation.objects.get(club_id = club_id)
                        context = {'team_info':team_info}
                        return render(request, 'team_info.html', context)
        form = TeamInformationForm()
        context = {'form':form}
        return render(request, 'team_information_form.html', context)         


