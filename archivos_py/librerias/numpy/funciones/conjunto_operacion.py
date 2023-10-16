
#'  OPERACIONES DE CONJUNTOS

#' Un conjunto matematico es una coleccion de elemntos unicos
#' Se usan para operaciones en las que se necesita la interseccion, union o diferencia

#' Para crear conjuntos en numpy se utiliza el metodo unique() sobre una matriz

#! La matriz solo puede ser de una dimencion 1D

# Convertir la siguiente matriz de elementos repetidos a un conjunto:

import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr) #* Devuelve el conjunto correspondiente de la matriz (elimina elementos repetidos)

# print(x)

#' Union: Se usa la función union1d()

#c Encontrar la union de los siguientes dos arreglos:

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2) #* Devuelve la union

# print(newarr)

#' Intersección: Se usa el metodo intersect1d()

#c Encontrar la intersección de los conjuntos:

#? El parametro assume_unique se deve establecer como True cuando se trate con conjuntos para acelerar el calculo

newarr_1 = np.intersect1d(arr1, arr2, assume_unique=True) #* Devuelve la intersección

# print(newarr_1)

#' Diferencia: Valores que esten presentes en alguno de los conjuntos pero no en el otro
#' Se utiliza la función setdiff1d()

#c Encontrar la diferencia entre los conjuntos:

newarr_2 = np.setdiff1d(arr1, arr2, assume_unique=True) #* Diferencia de arr1 - arr2

# print(newarr_2)

#' Diferencia simetrica: Encuentra los valores que no estan presentes en ambos conjuntos

#c Encontrar la diferencia simetrica de los conjutnos:

newarr_3 = np.setxor1d(arr1, arr2, assume_unique=True)

print(newarr_3)