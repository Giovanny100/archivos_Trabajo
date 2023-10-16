
#'  MINIMO COMUN MULTIPLO

#' Es el mas pequeño de los multiplos comunes entre un conjunto de numeros

import numpy as np

num1 = 4
num2 = 7


x = np.lcm(num1, num2)

# print(x)

#' Para encontrar mcm en matrices se puede usar el metodo reduce()
#' El metodo reduce(), usara la ufunct (lcm()), en cada elemento y reduce el arreglo en una dimensión

#c Encontrar el mcm de la siguiente matriz:

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)