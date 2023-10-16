
#'             LOGARITMOS NUMPY

#' Numpy provee funciones para realizar registros de base 2, 10 y e

#' LOGARITMOS BASE 2: Se puede usar la funcion los2()  para obtenerlo
#' LOGARITMOS BASE 10: Se puede usar la funcion log10()
#' LOGARITMO BASE e (NATURAL): Se puede usar la funcion log()

import numpy as np

arr = np.arange(1,10)
# print(np.log2(arr)) #* Devuelve el logaritmo base 2 de la matriz arr
# print(np.log10(arr)) #* Devuelve el logaritmo base 10 de la matriz arr
# print(np.log(arr)) #* Devuelve el logaritmonatural de la matriz arr

#'No existe una funcion que permita calcular el Logaritmo de cualquier base
#' Se puede crear la funcion con frompyfunc() con dos parametros de entrada y dos de salida

from math import log

# Convertir la función log en una función universal de numpy llamada uplog a traves de frompyfunc:

# Argumetos:
#a Primer argumento: Función que se va a convertir
#a Numero de argumentos de entrada
#a Numero de argumentos de salida

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15)) #* Devuelve el logaritmo base 15 de 100



