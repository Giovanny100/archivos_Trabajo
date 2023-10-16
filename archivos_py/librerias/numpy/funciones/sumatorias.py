
#' La principal diferencia entre una suma y una erroniamente llamda "sumatoria" es que la sumatoria es aplicable
#' Para n elemetnos (infinito)

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2]) #* Devuelve la sumatoria de los elemetos

#! La principal diferencia con add es que add hacia la suma de los elemtos de indice correspondientes

# print(newarr)

#' SUMAS SOBRE UN EJE
#' Si se especifica un eje entonces numpy hara la sumatoria de los elemtos de cada arreglo

newarr_1 = np.sum([arr1, arr2], axis =1) #* Suma de los elementos de cada arreglo por separado

# print(newarr_1)

#' SUMA ACUMULATIVA
#' Significa sumar parcialmente los elemetos de la matriz

#? La suma parcial de [1,2,3,4] seria [1,1+2,1+2+3,1+2+3+4] = [1,3,6,10]

arr = np.array([1,2,3])
newarr_2 = np.cumsum(arr)
print(newarr_2)