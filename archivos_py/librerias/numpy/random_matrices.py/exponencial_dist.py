
#'                 DISTRIBUCION EXPONENCIAL

#' Se utiliza para describir el tiempo hasta el proximo evento

#a Parametros:

#a sacale = inversa de la tasa (ver lam en distribucion de Poisson) por defecto 1,0
#a size = La forma de la matriz

#c Extraiga una muestra para distribución exponencial con escala 2.0 y tamaño 2x3:

from numpy import random

x = random.exponential(scale=2, size=(2, 3))

# print(x)

#c Visualización de distribución exponencial

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist=False)

plt.show()