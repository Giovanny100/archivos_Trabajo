
#' JSON es una sintaxis para almacenar e intercambiar datos.
#' JSON es texto escrito con notación de objetos JavaScript

#c Python tiene un paquete integrado llamado json, que se puede utilizar para trabajar con datos JSON.

import json

#' Si tiene una cadena JSON, puede analizarla utilizando el json.loads()método.

#' El resultado será un diccionario Python

#* Cualquier JSON:

x =  '{ "name":"John", "age":30, "city":"New York"}'

#* Analizar con sintaxis de python x:

y = json.loads(x)

#* El resultado será un diccionario:

print(y["age"])

#' Convertir de Python a JSON
#' Si tiene un objeto Python, puede convertirlo en una cadena JSON utilizando el json.dumps()método

#* Objeto pytohn (diccionario de python):

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#* Convertir a JSON:
y = json.dumps(x)

#* El resultado será un string JSON:

print(y)

#' Formatear el resultado
#' El ejemplo anterior imprime una cadena JSON, pero no es muy fácil de leer, sin sangrías ni saltos de línea.

#' El json.dumps()método tiene parámetros para facilitar la lectura del resultado:

#' Utilice el indentparámetro para definir el número de sangrías:

print(json.dumps(x, indent = 4))

#' Ordenar el resultado

#' Utilice el sort_keysparámetro para especificar si el resultado debe ordenarse o no:

print(json.dumps(x, indent=4, sort_keys=True))