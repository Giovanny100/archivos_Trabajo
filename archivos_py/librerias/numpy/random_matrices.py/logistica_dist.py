
#'          DISTRIBUCION LOGISTICA

#' Se utiliza para describir el crecimiento
#' Se utiliza ampliamente en machin learning,regresion logistica y redes neuronales

#' Tiene tres parámetros:

#a loc- es decir, dónde está el pico. Predeterminado 0.

#a scale- desviación estándar, la planitud de la distribución. Predeterminado 1.

#a size- La forma de la matriz devuelta.

#c Extraiga muestras de 2x3 de una distribución logística con media en 1 y stddev 2.0:

from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

#c Crear grafico de distribucion:

import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot(random.logistic(size=1000), hist=False)

# plt.show()

#' Diferencia entre distribución logística y normal
#' Ambas distribuciones son casi idénticas, pero la distribución logística tiene más área debajo de las colas, lo que significa que representa una mayor posibilidad de que ocurra un evento más alejado de la media.

#' Para un valor de escala más alto (desviación estándar), las distribuciones normal y logística son casi
#' idénticas, excepto el pico.

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()