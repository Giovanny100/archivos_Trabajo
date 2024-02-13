
#' DISTRIBUCIÓN NORMAL

#'Es una de las distribuciones mas importantes tambien llamada distribucion gausseana
#' Se ajusta a la distribucion de probabilidad de muchos eventos (puntuaciones de IQ, latidos de corazón)

#' Se puede usar el metodo random.normal() para obtener una ditribucion normal
#' Tiene tres parametros:

#a   loc = (media) pico de la campana
#a   sclale = (desviacion estandar) que tan plana esta la grafica
#a size = La forma de la matriz devuelta

#C Generar una distribución normal aleatroia de 2x3:

from numpy import random

x = random.normal(size=(2,3)) #*Por defecto se usa media = 0 y desv_est = 1 (valores cercanos a 0)

# print(x)

g = random.normal(loc=1, scale=2, size=(2, 3)) #* media = 1, desv_est = 2, matriz 2x3

# print(g)

#c Visualización de distribución normal

import matplotlib.pyplot as plt
import seaborn as sns

#? random.normal(size=1000): Genera una muestra de 1000 números aleatorios de una distribución normal (gaussiana)
#? estándar, es decir, con una media de 0 y una desviación estándar de 1.
sns.displot(random.normal(size=1000), hist=False) #*Distribucion normal

plt.show()