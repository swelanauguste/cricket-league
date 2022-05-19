from django.contrib import admin

from .models import HowOut, Match, MatchBatter, Venue

admin.site.register(MatchBatter)
admin.site.register(Match)
admin.site.register(HowOut)
admin.site.register(Venue)
