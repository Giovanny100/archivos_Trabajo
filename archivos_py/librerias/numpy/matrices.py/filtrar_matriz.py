
#' FILTRADO DE MATRICES

#'Filtrado: Obtener algunos elementos de una matriz existente y crear una nueva matriz a partir de ellos.
#'NumPy filtra una matriz utilizando una lista de índice booleano .
#'Una lista de índices booleanos es una lista de valores booleanos correspondientes a índices en la matriz.
#'Si el valor en un índice es True ese elemento está contenido en la matriz filtrada, si el valor en ese índice
#'es False ese elemento se excluye de la matriz filtrada.

#c Cree una matriz a partir de los elementos del índice 0 y 2:

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x] #* Da como salida los elementos del arr que son true en x

# print(newarr)

#' Creando la matriz de filtros:

#c En el ejemplo anterior codificamos los valores True y False
#c pero el uso común es crear una matriz de filtros basada en condiciones.

#Crearemos una matriz de filtros que solo tome los valores de la original que sean mayores que 42:

arr = np.array([41, 42, 43, 44])

filter_arr = [] #* Donde se almacenaran los valores de la matriz de filtros es decir True o False

for element in arr:
  if element > 42: #* Damos la condición
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

# print(filter_arr) #* Devuelve la matriz de boolenos para filtrar
# print(newarr) #* Da la matriz de valores ya filtrada

# Crear una matriz de filtros que devuelva solo los elementos pares:

m = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

filt = m % 2 == 0
newarr = m[filt]
print(newarr)