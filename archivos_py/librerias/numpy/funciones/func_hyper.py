
#'         FUNCIONES HIPERBOLICAS

#' Se cuentan con funciones sinh(),cosh(),tanh() que toman valores en radianes y devuelve el valor correspondient

#c Encontrar el valor del seno hiperbolico de pi/2:

import numpy as np

x = np.sinh(np.pi/2)

# print(x)

#c Encontrar el valor del coseno hiperbolico de una matriz:

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

d = np.cosh(arr)

# print(d)

#c Encontrar el valor del angulo de con funciones inversas de sinh,cosh,tanh

f = np.arcsinh(1.0)

# print(f)

#c Encontrar angulos para cada valor en las matrices:

arr_1 = np.array([0.1, 0.2, 0.5])

a = np.arctanh(arr_1)

# print(a)