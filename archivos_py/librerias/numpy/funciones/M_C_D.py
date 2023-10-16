
#' MAXIMO COMUN DENOMINADOR

#' Es el mas grande divisor comun entre dos o mas numeros

import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2) #* Devuelve MCD = 3 poque no hay otro numero mas grande que pueda dividir a 6 y 9

# print(x)

#' MCD en matrices

arr = np.array([20, 8, 32, 36, 16])

y = np.gcd.reduce(arr)

print(y)