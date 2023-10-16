
#' Unir significa poner el contenido de dos o más matrices en una sola matriz.
#' En SQL unimos tablas en función de una clave, mientras que en NumPy unimos arrays por ejes.

#' Pasamos una secuencia de arrays que queremos unir a la función concatenate(), junto con el eje.
#' Si el eje no se pasa explícitamente, se toma como 0.

#c Unir dos matrices:

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2)) #* Une las dos matirces con la funcion concatenate()

print(arr)

#c Une dos matrices 2-D a lo largo de filas (eje=1):


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1) #* Unimos las matrices con las respectivas filas

print(arr)

#c Unir matrices usando funciones de pila:

#' El apilamiento es lo mismo que la concatenación, la única diferencia es que el apilamiento se realiza a
#' lo largo de un nuevo eje.

#' Podemos concatenar dos matrices 1-D a lo largo del segundo eje, lo que daría como resultado colocarlas una
#' sobre la otra, es decir. apilado.

#' Pasamos una secuencia de arrays que queremos unir al método stack() junto con el eje.
#' Si el eje no se pasa explícitamente, se toma como 0.

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

#c Apilado a lo largo de filas
#' NumPy proporciona una función auxiliar: hstack() apilar a lo largo de filas.

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

#c Apilado a lo largo de columnas
# 'NumPy proporciona una función auxiliar: vstack()  apilar a lo largo de columnas.

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

#c Apilado a lo largo de la altura (profundidad)
#' NumPy proporciona una función auxiliar: dstack() apilar a lo largo de la altura, que es lo mismo que la profundidad.

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)