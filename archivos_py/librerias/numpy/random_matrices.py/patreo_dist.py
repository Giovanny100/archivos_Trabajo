
#'      DISTRIBUICION DE PARETO

#' Esta distribucion sigue la ley de Patreo (20% factores,80% resultado)

#a Parametros:

#a parametro de forma
#a Forma de la matriz

#c Sacar una muestra para la distribucion de patreo con forma de 2 y tamaño 2x3

from numpy import random

x = random.pareto(a = 2, size = (2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()