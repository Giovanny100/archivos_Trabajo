
#'              REDONDEO DE DECIMALES

#' Existen principalmente cinco formas de redondear decimales en Numpy:

#' Trunacamiento: Elimina los decimales y devuelve el numero flotante mas cercano a cero

import numpy as np

#c Truncar los elementos de la siguiente matriz:

arr_1 = np.trunc([-3.1666, 3.6667]) #* Se devolveran los enteros mas cercanos a cero (3)
arr_2 = np.fix([-3.1666, 3.6667]) #* Se devolveran los enteros mas cercanos a cero (3)
# print(arr_1, arr_2)

#' Redondeo: Redondea con base en si el decimal indicado es mayor o menor a 5

arr_3 = np.around(-3.1666,1) #* Redondea el numero con base en la cantidad de decimales del segundo argumento
# print(arr_3)

#' Floor: Redondea el decimal al entero inferior mas cercano

arr_4 = np.floor([-3.84552,3.485]) #* Devueve una matriz con los enteros mas pqueños y cercanos al decimal
# print(arr_4)

#' Ceil: Redondea el decimal al entero mas cercano y mayor

arr_5 = np.ceil([-3.3454,4.72696]) #* Devuelve el entero maximo mas cercano al decimal
print(arr_5)

