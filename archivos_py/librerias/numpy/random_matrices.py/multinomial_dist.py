
#'            DISTRIBUCION MULTINOMIAL

#' Es una generalizacion de la distribucion binomial (describe resultados de ecenarios multinomiales)
#' Donde los ecenarios deben ser solo uno de dos

#a Parametros:
#a n = numero de resultados posibles (ej. seis para tirar dados)
#a pvals = lista de probabilidades de resultados (ej. 1/6,1/6,1/6,1/6,1/6,1/6)
#a size = Forma de la matriz

#c Sacar la muestra para un lanzamiento de dados:

from numpy import random

x = random.multinomial(n =6, pvals =[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)