
#' Cree un archivo con el nombre urls.pyen la misma carpeta que el views.pyarchivo y escriba este
#' código en él:

#* from django.urls import path
#* from . import views

#* urlpatterns = [
#*     path('members/', views.members, name='members'),
#* ]

#' El urls.pyarchivo que acaba de crear es específico para la membersaplicación.mi_proyecto.
#'También tenemos que hacer algo de enrutamiento en el directorio raíz . Esto puede parecer complicado,
#' pero por ahora, simplemente sigue las instrucciones a continuación.
#' Hay un archivo llamado urls.py en la my_tennis_club carpeta, abra ese archivo y agregue el include
#' módulo en la importdeclaración, y también agregue una path()función en la urlpatterns[] lista, con
#' argumentos que enrutarán a los usuarios que ingresan a través de 127.0.0.1:8000/.

#' Entonces el archivo se vera así:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]