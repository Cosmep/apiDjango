from django.db import models

# Create your models here.
# Definimos el modelo de events

class Event(models.Model):
    event = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=85)
    date = models.DateField()

    def __str__(self):
        return self.event
    
class Contact(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    
   

