
#' PASO 1. CREAR UN NUEVO PROYECTO EN DJANGO

#c En la terminal navegar hasta la carpeta donde se va a crear el proyecto.
#c Ejecutar: django-admin startproject mywebsite

#? Lo anterior creara una carpeta llamada 'my website' con la estructura inicial de un ´rpyecto Django

#' PASO 2. CREAR UNA APLICACION EN DJANGO

#C En la misma termial navega al directorio recien creado 'my website' y ejecutar:

#* python manage.py startapp myapp

#? Lo anterior creara una aplicacion llamada myapp

#' PASO 3. DEFINE UNA VISTA

#c Abre el archivo 'myapp/ivews.py' y define una vista simple:

#* from django.shortcuts import render
#* from django.http import HttpResponse

#* def home(request):
#*     return HttpResponse("¡Hola, bienvenido a mi página web!")

#' PASO 4. CONFIGURAR LAS URLS

#C Abre el archivo myapp/urls.py y define las URLs para tu aplicación:

# from django.urls import path
# from myapp import views

# urlpatterns = [
#    path('', views.home, name='home'),
# ]

#' PASO 5. CONFIGURAR LAS URLS DEL PROYECTO.

#C Abre el archivo mywebsite/urls.py y configura las URLs del proyecto:

#* from django.contrib import admin
#* from django.urls import path, include

#* urlpatterns = [
#*     path('', include('myapp.urls')),
#*     path('admin/', admin.site.urls),
#* ]

#' PASO 6. EJECUTAR EL SERVIDOR DE DESARROYO.

#C En la terminal, dentro del directorio mywebsite, ejecuta:

#* python manage.py runserver

#' Abre tu navegador y visita http://127.0.0.1:8000/, deberías ver tu mensaje de bienvenida.