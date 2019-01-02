"""webprogramming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cricketclubinformation.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('player/registration/form/', player_registration, name = "player_registration"),
    path('contact/form/', contact, name = "contact"),
    path('club/registration/form/', club_registration, name = 'club_registraoin'),
    path('player/performance/form/', player_performance, name = 'player_performance'),
    path('match/information/form/', match_information, name = 'match_information' ),
    path('team/information/form/', team_information, name = 'team_information'),

]
