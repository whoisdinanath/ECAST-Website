from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'id']
    search_fields = ['title', 'date']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'for_event', 'id']
    search_fields = ['name', 'email', 'for_event__title']
