
#' ORDENAR MATRICES

#' Ordenar significa poner elementos en una secuencia ordenada .
#' Secuencia ordenada es cualquier secuencia que tiene un orden correspondiente a elementos,
#' como numérico o alfabético, ascendente o descendente.
#' El objeto NumPy ndarray tiene una función llamada sort() que ordenará una matriz específica.

#C Ordenar la matriz:
#! Tambien se pueden ordenar matrices de otros tipos de datos

import numpy as np

arr = np.array([3, 2, 0, 1]) #* Devuelve una copia de la matriz de menor a mayor


print(np.sort(arr))