
#'Una aplicación es una aplicación web que tiene un significado específico en su proyecto, como una página de inicio, un formulario de contacto o una base de datos de miembros.
#' En este tutorial crearemos una aplicación que nos permita enumerar y registrar miembros en una base de datos.
#' Pero primero, creemos una aplicación Django simple que muestre "¡Hola mundo!".

#' Crear aplicación
#'Le daré un nombre a mi aplicación members.
#' Comience navegando hasta la ubicación seleccionada donde desea almacenar la aplicación,
#' en mi caso la my_tennis_clubcarpeta, y ejecute el siguiente comando.
#' Si el servidor aún está ejecutándose y no puede escribir comandos, presione [CTRL] [BREAK]
#'o [CTRL] [C] para detener el servidor y debería estar nuevamente en el entorno virtual.

#* py manage.py startapp members

#' Django crea una carpeta nombrada membersen mi proyecto, con este contenido:

#* my_tennis_club
#*    manage.py
#*    my_tennis_club/
#*    members/
#*        migrations/
#*            __init__.py
#*        __init__.py
#*        admin.py
#*        apps.py
#*        models.py
#*        tests.py
#*        views.py


#'odos estos son archivos y carpetas con un significado específico. Aprenderá sobre la mayoría de ellos
#'más adelante en este tutorial.
#'Primero, eche un vistazo al archivo llamado views.py.
#' Aquí es donde recopilamos la información que necesitamos para enviar una respuesta adecuada.