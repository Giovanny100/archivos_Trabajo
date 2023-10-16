
#' La distribución de Chi Cuadrado se utiliza como base para verificar la hipótesis

#'Tiene dos parámetros:


#a df- (grado de libertad).

#a size- La forma de la matriz devuelta.

#c Extraiga una muestra para la distribución de chi cuadrado con grado de libertad 2 y tamaño 2x3:

from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x)

#c Visualización de la distribución de Chi cuadrado:

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()