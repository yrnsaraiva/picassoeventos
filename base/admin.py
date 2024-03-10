from django.contrib import admin

from .models import Event, PastEvents, FutureEvents

# Register your models here.

admin.site.register(Event)
admin.site.register(PastEvents)
admin.site.register(FutureEvents)

