
# # Creamos las rutas en un nuevo archivo dentro de views

# Importamos las vistas de la aplicación
# Ruta para crear evento
# Ruta para listar eventos
# Ruta para actualizar evento
 
from django.urls import path
from . import views  

urlpatterns = [
    path('create/', views.create_event, name='create_event'),  
    path('events/', views.event_list, name='event_list'), 
    path('events/update/<int:pk>/', views.update_event, name='update_event'),  
    path('contact/', views.create_contact, name='create_contact'), 
   
]
