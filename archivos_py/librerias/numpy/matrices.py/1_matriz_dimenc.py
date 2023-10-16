
#' Numpy (Numerical Python --> Python numerico) es una libreria ene python que sirve para trabajar con matrices
#' Tambien tiene funciones para trabaar en el domini de algebra lineal, tranfromadas de fourier y matrices

#'Las listas de python sirven para proponer arreglos de datos como las matrices pweo son lentas a la hora de procesarlas
#' Numpy proporciona arreglos (matrices) que son 50 veces mas rapido a la hora de procesarlas


import numpy as np

#* Para verificar la version de numpy:

# print(np.__version__) #? Devuelve la version de numpy

#* Para crear matrices en python se usa la palabra clave array como metodo del alias np:

matriz = np.array([1, 2, 3, 4, 5]) #? Se uso una lista para crear la matriz pero pueden ser tuplas
# print(matriz)

#* Revisar el tipo de dato:

# print(type(matriz))

#' Dimencion de las matrices (profundidad de los elementos, es decir que tan anidadas estan)

#* Matriz 0-D (escalares) son arreglos de una sola matriz:

arr_0 = np.array([5])
# print(arr_0)

#* Matriz 1-D (tienen matrices 0D (escalares) como elementos):

arr_1 = np.array([1, 2, 3,4,arr_0[0]])
# print(arr_1)

#* Matriz 2-D (tienen matrices 1D como elementos) se utilizan a menudo para representar matrices o tensores de 2do orden:

arr_2 = np.array([arr_1,arr_1])
# print(arr_2)

#* Matriz 3D (tienen matrices 2D como elementos):

arr_3 = np.array([[arr_2],[arr_2]])
print(arr_3)

#' Para comprobar la dimencion de la matriz se puede usar el metodo ndim

print(arr_0.ndim)

#' Crear una matriz dando como argumento la dimencion:

arr_6 = np.array([1,2,3,4,5,6,7,8,9,10], ndmin = 6)
print(arr_6)
print('Numero de dimenciones:', arr_6.ndim)
