from django.contrib import admin

from .models import BattingStyle, BowlingStyle, Player

admin.site.register(BattingStyle)
admin.site.register(BowlingStyle)
admin.site.register(Player)