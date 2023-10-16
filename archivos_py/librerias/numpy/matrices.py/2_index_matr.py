
#' Se puede acceder a los elementos de una matriz por medi de los indices:

import numpy as np

x = np.array([1, 2, 3, 4])

# print(x[2])

#' Se puede pedir dos elementos de una matriz tambien y operar con ellos:

# print(x[1] + x[3])

#' Cuando la matriz es de mayor orden se debe espcificar dos posiciones de argumento en los indices:

# y = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12)])
# print('El 3er elemento de la 2da fila es:', y[1,2])

#' Se puede cambiar de forma (dimenciones) una matriz o bien reordenarla:

#c Ejemplo: Cambiar una matriz 1D a 2D

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(4,3) #* Convierte la matriz a una de 4 filas 3 columnas
# newarr_2 = arr.reshape(2,3,2) #* Convierte la matriz a una de 2 filas
# print(newarr)
# print(newarr_2)

#' Se permite tener una dimencion desconocida, significa que no tienes que especificar un numero exacto de dimenciones
#' Pasa como valor -1 y numpy lo calculara automaticamente por ti

arreglo = np.array([1,2,3,4,5,6,7,8])
re_ord = arreglo.reshape(2,2,-1) #* Devuelve una matriz 2x2
print(re_ord)

#'Podemos hacer arreglos multidimensionales a matrices de una sola dimension:

arr_3 = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(arr_3.reshape(-1))