from wsgiref import validate
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Event
from .forms import EventForm, ContactForm


# Implementamos las vistas

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


# Obtener los eventos de la base de datos
def event_list(request):
    events = Event.objects.all().order_by('-id')
    
    if request.method == 'POST' and 'delete' in request.POST:
        event_id = request.POST['event_id']
        event = get_object_or_404(Event, pk=event_id)
        event.delete()  
        return redirect('event_list') 
    return render(request, 'event_list.html', {'events': events})


def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return redirect('index')

# Guarda los cambios en la base de datos
# Redirige a la lista de eventos
def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    if request.method == "POST":
        event.event = request.POST.get('event')
        event.category = request.POST.get('category')
        event.date = request.POST.get('date')
        event.save()  
        return redirect('event_list')  

    return render(request, 'update_event.html', {'event': event})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print('resultado de form', form)
        if form.is_valid():
            print('entro a validate')
           
            print( form.save())
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'create_contact.html', {'form': form})