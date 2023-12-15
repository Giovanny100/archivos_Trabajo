
#' DJANGO: Es una esreuctura de trabajo para crear sitios web con python (Util para sitios web con BD)
#' Django facilita las cosas dificiles para que el usuario se dedique a crear apps o paginas web
#' Enfatiza en la reutilización de los componetnes conocida como DRY (Don´t Repite Yourself), viene con
#' fuciones listas como:

#c Sistema de inicio de sesión
#c Conexion a base de datos
#c Operaciones CRUD (Crear,Leer,Actualizar,Eliminar)

#' Sigue el patron de diseño MVT (Model View Template)

#c Modelo: Los datos que desea presentar, generalmente datos de una base de datos.
#c Vista: Un controlador de solicitudes que devuelve una plantilla y el contenido relevantes, segun la solicitud
#C Plantilla: Un archivo de texto (como un archivo HTML) que contiene el diseño de la página web, con logica de como mostrar los datos

#' MODELO: Proporciona los datos de la BD. En Django se entregan como un mapeo relacional de objetos (ORM).
#'ORM: Técnica para facilitar el trabajo con base de datos.
#'Generalmente la forma mas común es extraerlos de una BD SQL pero esta requiere de conocimientos extensos de manejo de la base de datos SQL
#'Trabajar con Djngo ORM facilita la comunicación de la BD sin escribir sentencias complejas de SQL
#' Los modelos suelen estar ubicados en un archivo llamado 'models.py'

#' VISTA: Método que toma solicitudes http como argumentos, importa los modelos reelevantes, descubre que datos
#' enviar a la plantilla y da el resultado final. Las vistas estan ubicadas en un archivo views.py

#' PLANTILLAS: Archivo donde se descrive como se debera represntar el resultado.Suelen ser archivos .html
#' con codigo HTML que describe el diseño de una pagina web, pero tambien pueden estar en otros formatos de archivos para representar otros resultados.
#' Django usa HTML para describir el diseño, pero usa etiquetas de Django para agregar lógica.

#'Las plantillas de una app se encuentran en una carpeta llamada templates

#' URL: Cuando un usuario solicita una URL, Django decide que visita le enviará. Archivo llamado urls.py

#' 1. Django recibe la URL, verifica el urls.pyarchivo y llama a la vista que coincide con la URL.
#' 2. La vista, ubicada en views.py, busca modelos relevantes.
#' 3. Los modelos se importan desde el models.pyarchivo.
#' 4. Luego, la vista envía los datos a una plantilla especificada en la templatecarpeta.
#' 5. La plantilla contiene etiquetas HTML y Django, y con los datos devuelve el contenido HTML terminado al navegador.


#c Una vez que haya encontrado un nombre adecuado para su proyecto Django, como el mío: my_proyecto,
#c navegue hasta el lugar del sistema de archivos donde desea almacenar el código (en el entorno virtual),
#c navegaré hasta la myworldcarpeta y ejecutaré este comando en el símbolo del sistema:

#* django-admin startproject my_tennis_club

#c Django crea una my_tennis_clubcarpeta en mi computadora, con este contenido:

#*my_tennis_club
#*   manage.py
#*    my_tennis_club/
#*        __init__.py
#*        asgi.py
#*        settings.py
#*        urls.py
#*        wsgi.py

#' Todos estos son archivos y carpetas con un significado específico; aprenderá sobre algunos de ellos más
#' adelante en este tutorial, pero por ahora, es más importante saber que esta es la ubicación de su
#' proyecto y que puede comenzar a crear aplicaciones en él.

#' Ejecute el proyecto Django
#' Ahora que tienes un proyecto Django, puedes ejecutarlo y ver cómo se ve en un navegador.

#c Navegue a la /my_tennis_clubcarpeta y ejecute este comando en el símbolo del sistema:

#* py manage.py runserver

#c Abra una nueva ventana del navegador y escriba 127.0.0.1:8000en la barra de direcciones.

#? Debera aparecer una ventana en el navegador