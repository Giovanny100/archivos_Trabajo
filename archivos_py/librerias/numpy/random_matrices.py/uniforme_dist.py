
#'                        DISTRIBUCION UNIFORME

#' Se utiliza para describir la probabilidad de que cada evento tenga las mismas posibilidades de ocurrir.

#' Tiene tres parámetros:

#a a- límite inferior - valor predeterminado 0

#a b- límite superior - predeterminado 1

#a size- La forma de la matriz devuelta.

# Cree una muestra de distribución uniforme de 2x3:

from numpy import random

x = random.uniform(size=(2, 3))

print(x)

# Crear la grafica de distribucion uniforme de los datos:

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()