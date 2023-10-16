
#'           DISTRIBUCION DE POISSON

#'Es una distribucion discreta. Estima cuantas veces puede ocurrir un evento en un tiempo especifico.
#' Tiene dos parametros:

#a lam = tasa o numero conocido de ocurrencias(media)
#a size = La forma de la matriz devuelta

from numpy import random
x = random.poisson(lam = 2, size = 1000) #* Genera datos de distribucion de poisson
# print(x)

#c Mostrar la grafica de distribucion:

import seaborn as sns
import matplotlib.pyplot as plt

# sns.distplot(random.poisson(lam=2, size=1000), kde=False) #* Genera el histogrma para los datos

# plt.show()

#c Comparacion de Distribucion normal y poisson:

#! Para una distribución de Poisson lo suficientemente grande, se volverá similar a la distribución normal
#! con cierta media y desarrollo estándar.

# sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
# sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

# plt.show()

# Comparacion de distribucion binomial y poisson:

#! La distribución binomial solo tiene dos resultados posibles, mientras que la distribución de Poisson
#! puede tener resultados posibles ilimitados.

#! Pero para casos muy grandes ny cercanos a cero, pla distribución binomial es casi idéntica a la distribución
# ! de Poisson, tal que n * p es casi igual a lam.

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()