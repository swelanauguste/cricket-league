from django.contrib import admin

from .models import Year, Version, Tournament

admin.site.register(Year)
admin.site.register(Version)
admin.site.register(Tournament)
