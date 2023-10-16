
#'               DISTRIBUCION RAYLEIGH

#' Es utilizada para el procesamiento de señales

#a Parametros:

#a scale (desviacion estandar) deicide que tan plana sera la distribucion (por defecto 1)
#a size = tamaño de la matriz

#c Extraer una muestra para la distribución Rayleigh

from numpy import random

x = random.rayleigh(scale=2, size= (2,3))
# print(x)

#c Visualización de la distribución de Rayleigh:

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()