
#'                        FUNCIONES TRIGONOMETRICAS

#' Numpy proporciona funciones como sin(), cos(), tan() que toman valores en radianes y produce el correspondiente
#' valor de las funciones seno coseno y tangente

import numpy as np

x = np.sin(np.pi/2)

# print(x)

#c Encontrar el seno de los valores de una matriz:

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

y = np.sin(arr)

# print(y)

#' Convertir de grados a radianes. Por defecto se usan radianes como argumentos de las trigonometricas
#' Pero se puede convertir radianes a grados en Numpy

#c Convertir todos los valores (grados) de el siguiente arreglo a radianes:

arr = np.array([90, 180, 270, 360])

g = np.deg2rad(arr) #? Para la conversion inversa se utiliza la misma funcion al reves rad2deg

# print(g)

#' Encontrar angulos: Se utilizan las funciones trigonometricas inversas (arcsin,arccos,arctan)
#' Numpy proporciona ufuncs:

# arcsin(),arccos(),arctan()

#c Encontrar los agulos para los valores de seno correspondiente:

arr_1 = np.array([1,-1, 0.1])

y = np.arcsin(arr_1) #* Genera matriz de angulos correpondientes a los sen de los valores de la matriz

print(y)
