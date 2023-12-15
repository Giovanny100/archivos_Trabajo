
#' VISTAS DJANGO

#' Son funciones en python que reciben solictudes http y devuelven una respuesta http, como documentos HTTP
#' Una pagian que usa Django esta llena de vistas con diferentes tareas y misiones.

#' Las vistas se colocan en un archivo views.py ubicado en su carpeta de aplicacion
#' Hay un views.py en la carpeta creada members que se parece a lo siguiente:

#* y_tennis_club/members/views.py:

#* from django.shortcuts import render

#* Create your views here.

#'Encuéntrelo, ábralo y reemplace el contenido con esto:

#* from django.shortcuts import render
#* from django.http import HttpResponse

#* def members(request):
#*     return HttpResponse("Hello world!")

#' Nota: El nombre de la vista no tiene que ser el mismo que el de la aplicación.
#' Lo llamo membersporque creo que encaja bien en este contexto.
#' Este es un ejemplo sencillo sobre cómo enviar una respuesta al navegador.
#' Pero ¿cómo podemos ejecutar la vista? Bueno, debemos llamar a la vista a través de una URL.