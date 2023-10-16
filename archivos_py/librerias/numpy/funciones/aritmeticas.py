
#'             ARITMETICA SIMPLE

#' En lugar de utilizar los operadores normales(/ * + -) hay funciones que toman cualquier elemento iterativo
#' y realizan aritmetica condicionalamente

#' Significa que podemos definir condiciones donde debe de ocurrir la operacion aritmetica
#' Todas tomanun parametro where

#'SUMA: funcion add() suma los contenidos de las matrices y da una nueva con las sumas
#' SUBTRACT: funcion de resta de matrices
#' MULTIPLY: funcion de multiplicacion de matrices
#' DIVIDE: funcion de cociente de matrices
#' POWER: funcion de potencia de matrices
#' MOD and REMAINDER: Ambas devuelven el resto de los valores en el primer arreglo correspondientes al segundo arr
#' DIVMOD: Devuelve el cociente y el residuo, la primer matriz contiene el cociente y la segunda el residuo
#' ABSOLUTE and ABS: Funciones de valor absoluto
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 5, 3, 4, 5])
arr3 = np.array([2, -1, 5,- 3, 4,- 5])

newarr_1 = np.subtract(arr1, arr2) #* Resta el arr1 - arr2
newarr_2 = np.multiply(arr1, arr2) #* Multiplication arr1*arr2
newarr_3 = np.divide(arr1, arr2) #* Divide arr1/arr2
newarr_4 = np.power(arr1, arr2) #* Eleva los elementos del arrr1 a la potencia correspondiente del arr2
newarr_5 = np.mod(arr1, arr2) #* Devuelve el resto de vividir arr1%arr2
newarr_6 = np.divmod(arr1, arr2) #* Devuelve dos matrices una de cocientes y otra de residuos
newarr_7 = np.absolute(arr3) #* Devuelve los valores absolutos de una matriz

# print(newarr_1)
# print(newarr_2)
# print(newarr_3)
# print(newarr_4)
# print(newarr_5)
# print(newarr_6)

