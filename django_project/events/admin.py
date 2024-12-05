from django.contrib import admin
from .models import Event

# Registro básico del modelo Event en el admin de Django
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event', 'category', 'date') 
    search_fields = ('event', 'category')         