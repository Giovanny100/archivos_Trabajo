
#' PERMUTACION ALEATORIA DE ELEMENTOS

#' Unas permutacion se refiere a una posible forma de acomodar un determinado nuemro de datos
#' Ej. [3,2,1] es una permutación de [1,2,3] y vice-versa

#' El modumo random provee dos metodos para permutar: shuffle() y permutation()

#C Mezclando matrices (cambios sobre la misma matriz):

#' Mezclar significa cambiar la disposición de los elemetos en el lugar es decir dentro de la matriz

import numpy as np
from numpy import random

arr = np.array([1,2,3,4,5])

random.shuffle(arr) #* Cambiara el orden de los elemntos en la misma matriz definida (arr)
# print(arr)

#C Permutacion de matrices:

print(random.permutation(arr)) #* El metodo devuelve una nueva matriz reorganizada dejando la orignal sin cambios

