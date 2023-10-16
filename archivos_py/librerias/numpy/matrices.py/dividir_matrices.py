
#'Dividir matrices NumPy
#'Dividir es una operación inversa a unir.

#'La unión fusiona varias matrices en una y la división divide una matriz en varias.

#'Usamos array_split() para dividir matrices, le pasamos la matriz que queremos dividir y el número de divisiones.


#cDivida la matriz en 3 partes:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

#' Si la matriz tiene menos elementos de los necesarios, se ajustará desde el final en consecuencia.
#'Divida la matriz en 4 partes:

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)
