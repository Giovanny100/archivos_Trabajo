
#' Para encontrar el producto de la matriz de un producto, se puede utilizar la funcion prod()

import numpy as np

arr = np.array([1, 2, 3, 4])
x = np.prod(arr) #* Producto de todos los elementos de la matriz
# print(x)

#' Tambien se puede encontrar el producto de los elementos de dos matrices

arr1 = np.array([5, 6, 7, 8])

y = np.prod([arr,arr1]) #* Devuelve el producto de todos los elementos de las dos matrices
# print(y)

#' Tambien se puede encontrar el producto de las matrices individuales:

newarr = np.prod([arr, arr1], axis=1)
print(newarr)

#'Producto acumulativo

arr_prod = np.cumprod(arr1) #* Producto acumulado de los elementos
print(arr_prod)