
#'              DISTRIBUCION BINOMIAL

#' Es una distribucion discreta (es o no es/ no puede ser a medias) --> Datos discretos
#' Describe el resultado de escenarios binarios como volados o vivo muerto

#' Tiene tres parametros:

#a n = número de intentos
#a p = probabilidad de ocurrencia
#a size = Forma de la matriz devuelta (cantidad de numeros dentro de la matriz)

#c Ejemplo: Dados 10 intentos de lanzamiento de moneda se genran 10 puntos de datos:

from numpy import random

x = random.binomial(n = 10, p = 0.5, size = 1000)

# print(x)

#c Visualizar la distribucion de los datos:

import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False) #* Genera histograma

# plt.show()

#' La principal diferencia entre distribución normal y binomial es que la normal es continua y binomial discreta
#' Si se tienen suficiente datos n--> oo entonces la binomial parece ser normal

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()