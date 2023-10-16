
#'SON UNA POTENTE HERRAMIENTA PARA PARA VARIAS CLASES DE MANIPULACION DE CADENAS.
#'SON UN LENGUAJE ESPECIFICO DE DOMINIO (DSL POR SUS SIGLAS EN INGLES) QUE ESTA PRECENTE COMO UNA BIBLIOTECA EN LA MAYORIA DE LOS LENGUAJES DE PROGRAMACION, NO SOLO EN PYTHON.

#'SON UTILES PARA TAREAS PRINCIPALES:

#' -VERIFICAR QUE LAS CADENAS CORRESPONDAN A UN PATRON (POR EJEMPLO QUE UNA CADENA TENGA EL FORMATO DE UN CORREO ELECTRONICO);
#' -REALIZAR SUSTITUCIONES EN UNA CADENA  (POR EJEMPLO CAMBIAR LA ORTOGRAFIA DEL INGLES ESTADOUNIDENSE AL INGLES BRITANICO).
#' LOS LENGUAJES ESPECIFICOS DEL DOMINIO SON MINI-LENGUAJES DE PROGRAMACION ALTAMENTE ESPECIALIZADOS.
#' LAS EXPRESIONES REGULARES SON UN EJEMPLO POPULAR, Y SQL (PARA LA MANIPULACION DE BASE DE DATOS) ES OTRO.
#' LENGUAJES PRIVADOS ESPECIFICOS DEL DOMINIO SON A MENUDO UTILIZADOS PARA PROPOSITOS INDUSTRIALES PARTICULARES.
#' PUEDEN SER ACCEDIDAS UTILIZANDO EL MODULO re, EL CUAL ES PARTE DE LA BIBLIOTECA ESTANDAR.
#' LUEGO DE DEFINIR UNA EXPRESION REGULAR, LA FUNCION re.match PUEDE UTILIZARSE PARA VER SI CORESPONDE AL PRINCIPIO DE UNA CADENA.
#' SI ENCUENTRA UNA CORRESPONDENCIA, match DEVUELVE UN OBJETO QUE REPRECENTE LA COINCIDENCIA, SI NO, DEVUELVE NONE.
#' SE RECOMIENDA UTILIZAR CADENAS PURAS PARA EVITAR CONFUCIONES TAL COMO r"expresion"
#' LAS CADENAS PURAS NO ESCAPAN NADA, LO CUAL HACE MAS FACIL EL USO DE EXPRESIONES REGULARES.


import re
pattern = r"spam"  #* La r antepuesta de en el string es para formar un texto crudo 'raw' quiere decir que no sera necesario escapara caracteres especiales

# print(re.match(pattern, "spamspam")) #* Devuelve el objeto almacenado con el cual hay coincidencia


#  #' OTRAS FUNCIONES PARA CORRESPONDER PATRONES SON re.search Y re.findall.

#  #* search: ENCUENTRA UNA CORRESPONDENCIA DE UN PATRON EN CUALQUIER CADENA.
#  #* findall: DEVUELVE UNA LISTA CON TODAS LAS SUBCADENAS QUE COINCIDEN CON UN PATRON.


# print(re.search(pattern, "spam")) #*  #* Devuelve el objeto almacenado con el cual hay coincidencia



# print(re.findall(pattern, "eggspamsausagespa")) #* Devuelve la lista con los elementos de coincidencia



# #' La busqueda regex devuelve un objeto con varios metodos que dan detalles sobre esta.
# #' estos metodo incluyen group que devuelve la cadena que coincide, start y end  que devuelven la posicion inicial y final de la cadena que coincide respectivamente
# #' y spam  que devuelve la posicion incicial y final como una tupla.


# pattern1 = r"pamas"

# match = re.search(pattern1, "eddspamasausagpamaspamas")

# if match:
#     print(match.group()) #* Cadena de colioncidencia
#     print(match.start()) #* Indice inicial en donde se encontro la cadena
#     print(match.end())  #* Devuelve el indice en donde termina la cadena
#     print(match.span()) #* Devuelve una tupla con el indice donde comienza y donde termina la cadena


# #' Uno de los metodos mas regulares es sub: remplaza todas las ocurrencias de uns cadena con repl, sustituyendo todas las ocurrencias hasta que count sea provisto.
# #' este metodo devuelve una cadena modificada.


str = "My name is Giovanny. Hola Giovanny"
pattern2 = r"Giovanny"
newstr = re.sub(pattern2, "Amy", str) #sustituyo giovanny por Amy
print(newstr)