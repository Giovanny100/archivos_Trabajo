
#' Histograma: Muestra distribuciones de frecuencias
#' Muestra el numero de observaciones con cada intervalo dado

#' En matplotlib se usa hist() la cual necesita una matriz de numeros para crear el histograma

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(127,5,1000) #* (media, desviacion,#valores)
# print(x)

plt.hist(x)
plt.show()