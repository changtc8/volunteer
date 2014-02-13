from django.contrib import admin
from users.models import User, Event, Ecalendar

class EventInline(admin.TabularInline):
     model = Event
     extra = 1

class UserAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name']
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ['first_name']
    inlines = [EventInline]

class EcalendarAdmin(admin.ModelAdmin):
    list_filter = ['date', 'time']
    list_display = ('date', 'time')
    search_fields = ['date']
    inlines = [EventInline]

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Ecalendar, EcalendarAdmin)
