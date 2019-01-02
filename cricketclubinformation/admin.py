from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Membership)
admin.site.register(PlayerRegistration)
admin.site.register(Contact)
admin.site.register(ClubRegistratoin)
admin.site.register(PlayersPerformance)
admin.site.register(MatchInformation)