
# Creamos un formulario para gestionar los eventos

from django import forms
from .models import Event
from .models import Contact

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event', 'category', 'date']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'telefono']