
#' NUMEROS ALEATORIOS EN NUMPY

#' Un numero aleatorio no signfica que sea diferente en cada ocacion si no mas bien se refiere al concepto estadistico
#' Aleatoriedad se refiere a que no se puede predecir logicamente

#' Existen elementos alaeatorios y pseudoaleatorios

#' Las computadoras trabajan con programas, y los programas son conjuntos de instrucciones
#' Deberia existir un programa para generar un numero aleatorio
#' Si existiera dicho programa se podria predecir por lo que no seria completamente aleatorio

#a Los numeros aleatorios generados mediante un algoritmo de generacion se llaman pseudoaleatorios

#? ¿Se pueden hacer numeros verdadramente aleatorios?

#'Si, para generar datos aleatorios en nuestra computadora necesitamos obtener datos random de alguna fuente externa
#'Estas fuentes externas son a menudo nuestras teclas o mouse o datos de la red

#! Para fines de seguridad se requieren datos completamente aleatorios (claves de cifrado)

#' Aqui se usaran numeros preudoaleatorios

#c Genere un numero entero del 0 al 100:

import numpy as np

from numpy import random

x = np.random.randint(100) #* Genera un entero aleatorio entre 0 y 100
# print(x)

#c Gemerar un float aleatorio

y = np.random.rand() #* Genera un float aleatorio entre 0 y 1
# print(y)

#c Generar matriz aleatoria:

#c El randint()método toma un size parámetro donde puede especificar la forma de una matriz.
#c Genere una matriz 1-D que contenga 5 números enteros aleatorios del 0 al 100:

mat=random.randint(100, size=(5)) #* Genera matriz con elementros entre 0 y 100 con cinco elementos

# print(mat)

#c Genere una matriz 2-D con 3 filas, cada fila contiene 5 números enteros aleatorios del 0 al 100:

r = random.randint(100, size=(3, 5))#* 100 limite superior,3 filas,5elementos por fila

# print(r)

#c Generar número aleatorio a partir de una matriz

#' El método choice() le permite generar un valor aleatorio basado en una matriz de valores.
#' El método choice() toma una matriz como parámetro y devuelve aleatoriamente uno de los valores.

x = random.choice([3, 5, 7, 9]) #* Devuelve alguno de los elementos de la matriz

# print(x)

#c Devuelve uno de los valores de una matriz:
#* size(filas,columnas)
x = random.choice([3, 5, 7, 9],size=(3, 5)) #* Cuando se especifica size entonces se genera una matriz

print(x)
