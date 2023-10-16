
#' Las matrices en Numpy se puden iterar analogamente como las listas u otros arreglos de python

import numpy as np

# x = np.array([1,2,3,4])
# for i in x:
#     print(i)

#' Si queremo iterar sobre cada elemento de matrices multidimensionales debemos usar varios for
#! De lo contrario se devolveran solo las matrices dentro de la matriz mas externa

# y = np.array([[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]])
# print(y.ndim)
# for e in y:
#     print(e) #* Al iterar sobre la matriz multidimensional se dan las matrices internas

#* En lugar podemos utilizar for anidados:

# for e in y:
#     for f in e:
#         for g in f:
#             print(g) #?Dado que es una de 3 dimensiones se utilizaron 3 iteradores para llegar a los elementos

#c Para iterar sobre arreglos de varias n dimensiones infinitas no seria factible usar n cantidad de for
#' Podemos usar la funcion nditer() para facilitar el trabajo:

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr): #* Nos dara directamente una iteracion sobre los elementos de cada matriz
#   print(x)

#' ITERAR MATRICES CON DIFERENTES TIPOS DE DATOS:

#' Podemos usar op_dtypes ydarle como arguymento el tipo de datos que queremos mientras iteramos
#' NumPy no cambia el tipo de datos del elemento en el lugar (donde el elemento está en una matriz), por lo que
#' necesita otro espacio para realizar esta acción, ese espacio adicional se llama buffer, y para habilitarlo
#' nditer()pasamos flags=['buffered'].

#c Iterar a través de la matriz como una cadena:

# import numpy as np

# arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)


#c Iterando con diferentes tamaños de paso:

#' Podemos usar filtrado y seguido de iteración.
#'Itere a través de cada elemento escalar de la matriz 2D omitiendo 1 elemento:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
