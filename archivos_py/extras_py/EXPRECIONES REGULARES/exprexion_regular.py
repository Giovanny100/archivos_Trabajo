
#' Una RegEx, o expresión regular, es una secuencia de caracteres que forma un patrón de búsqueda.

#' RegEx se puede utilizar para comprobar si una cadena contiene el patrón de búsqueda especificado.
#' Python tiene un paquete integrado llamado re, que puede usarse para trabajar con expresiones regulares.

#' Importar el remódulo:

import re

#? Ejemplo 1: Busque en una cadena para saber si comienza con "The" y termina con "Spain":

txt_1 = "The rain in Spain"
x = re.search("^The.*Spain$", txt_1)

if x: #* Esta linea es para que se ejecute siempre que x sea True
    print('El string comienza con "The" y termina con "Spain"')

else:
    print('El string no cumple')

print(re.findall('in',txt_1)) #* Devuelve una lista con todas las coincidencias encontradas
print(re.search('The',txt_1)) #* Devuelve el objeto con el que se hizo match
print(re. split(' ', txt_1))#* Devuelve una lista con la cadena dividida en cada coincidencia


