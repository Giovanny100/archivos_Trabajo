
#'                   DISTRIBUCION ZIPF

#' Muestrea datos segun la ley de zipf

#? Ley de zipf: en una colección, el enésimo término común es 1/n veces el término más común.
#?Por ejemplo, la quinta palabra más común en inglés aparece casi 1/5 veces más que la palabra más común.

#a Paramtros:

#a a = parametros de distribution
#a size =  forma de la matriz

#c Extraiga una muestra para la distribución zipf con el parámetro de distribución 2 con tamaño 2x3:

from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)

#c Visualización de la distribución Zipf

#c Muestre 1000 puntos, pero trace solo aquellos con valor <10 para obtener un gráfico más significativo.

import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()