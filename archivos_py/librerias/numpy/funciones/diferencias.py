
#' Una diferencia discreta significa restar dos elemetos sucesivos

#? Para [1,2,3,4] la diferencia discreta seria: [2-1,3-2,4-3] = [1,1,1]

#' Para encontrar esta diferencia discreta se usa la función diff()

import numpy as np

arr = np.array([10,15,25,5])

newarr = np.diff(arr) #* Devuelve la diferencia discreta de los elementos
print(newarr)

#' Si se especifica el parametro n entonces se hara la cantidad de veces n sobre las matrices resultantes

newarr1 = np.diff(arr, n = 2) #* Devolvera la diferencia discreta aplicada dos veces sobre los resultados
print(newarr1)
