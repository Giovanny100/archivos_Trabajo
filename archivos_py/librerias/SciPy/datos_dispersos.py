
#' DATOS DISPERSOS

#' Son datos que tienen en su mayoria datos no utilizados (elementos que no contienen ninguna informacion)

#? Datos dispersos: Conjunto de datos donde la mayoria de los valores son cero
#? Matriz densa: Es lo contrario de un matriz dispersa, la mayoria de los valores no son cero

#' En algebra computacional cuando trabajamos con derivadas parciales nos encontramos con datos dispersos

#' TRABAJAR CON DATOS DISPERSOS

#'Scipy tiene el modulo scipy.sparse que da funciones para tratar con datos dispersos
#' Hay principalmente dos tipos de matrices dispersas que usaremos

#?Las siguientes matrices se usan para ahorrar espacio de almacenamiento y mejorar la eficiencia computacional:

#' CSC: Columna Dispersa Comprimida; Para aritmetica eficiente
#' CSR: Fila Dispersa Comprimida; Para un corte de filas mas rapido, productos vectoiales de matriz mas rapidos

# Crear una matriz CSR a partir de una matriz:

import numpy as np
from scipy.sparse import csr_matrix
# arr = np.array([0,0,0,0,0,1,1,0,2])

# print(csr_matrix(arr))

#* El resultado mostrado es:
#*  (0, 5)        1 Muestra que hay un numero 1 en la fila 0 y columna 5
#*  (0, 6)        1 Muestra que hay un numero 1 en la fila 0 y columna 6
#*  (0, 8)        2 Muestra que hay un numero 0 en la fila 0 y columna 8

#? En una matriz dispersa, la mayoría de los elementos son cero, y almacenar todos esos ceros ocuparía mucho
#? espacio en memoria. Por lo tanto, se emplean formatos de representación dispersa que solo almacenan la
#? información relevante (es decir, los elementos distintos de cero) junto con suficiente información para
#? reconstruir la matriz original.

#' METODOS PARA MATRICES DISPERSAS

#c Ver datos almacenados sin los elementos ceros con la propiedad data:

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

# print(csr_matrix(arr).data) #* Muestra una matriz con los datos diferentes de cero

#c Metodo count_nonzero():

# print(csr_matrix(arr).count_nonzero()) #* Devuelve el numero de elementos que son diferentes de cero

#c Remover entradas cero de la martiz con el metodo eliminate_zeros()

mat = csr_matrix(arr)
mat.eliminate_zeros()

print(mat)