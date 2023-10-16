
#' Se puede buscar en una matriz un valor determinado y genrar el indice donde se encuentra:
#' Para buscar en un arreglo se usa el metodo where()

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4) #* Genera una tupla con los indices de los valores que coinciden con  4

print(x)

#' Impares:

arr_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

y = np.where(arr_1%2 == 1)

print(y)

#' Existe un método llamado searchsorted() que realiza una búsqueda binaria en la matriz y devuelve el índice
#' donde se insertaría el valor especificado para mantener el orden de búsqueda.

arr_2 = np.array([6, 7, 8, 9])

r = np.searchsorted(arr_2, 7)

print(r)