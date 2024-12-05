#PRIMEROS PASOS

#Crear el entorno virtual venv
python -m venv .venv 
#Activar el entorno virtual venv
.\.venv\Scripts\activate  

#INSTALACIONES DE MODULOS DEPENDENCIAS
leer el archivo requirements.txt


#Es el framework web con el que se manejara el crud (Capa de personalizacion)  
pip install django

#Para ver la version de django isntalada. 
django-admin --version

#Para crear la carpeta del proyecto django. 
django-admin startproject "NOMBREDELPROYECTO". 

#Para crear carpetas "aplicaciones" de django
python manage.py startapp "NOMBREDELAPP"

django_project/

#Ir a la carpeta djangocrud luego a settings.py ahi se direigen a INSTALLED_APPS y al final con comillas simples colocan el nombre de la app o carperta que se creo, hacer esto con todas las apps que se crean.

#Ir a la carpeta djangocrud luego a urls.py ahi importan de la carpeta task el archivo views y hacen una ruta 
path ('', views.helloworld) y ejecutan runserver para probar si funciona

#Define el modelo Event
#Crea un formulario para gestionar eventos.
#Implementa las vistas.
#Define las rutas
#Crea la interfaz gráfica

#Crear super usuario
python manage.py createsuperuser

#Correr servidor
python .\app.py runserver