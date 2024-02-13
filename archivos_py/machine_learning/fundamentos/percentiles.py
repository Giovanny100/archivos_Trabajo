
#' PERCENTILES

#' Es un valor que divide un conjunto de datos ordenados en 100 partes iguales
#' Representa la posición relativa de un valor en relación con el total de datos
#'Sirven para exprear que porcentaje de los datos esta por debajo o encima de este mismo

#' Los percentiles son comúnmente utilizados para entender la distribución de datos en una población o muestra. Algunos percentiles específicos incluyen:

#' Mediana (Percentil 50):

#' Divide los datos en dos partes iguales. El 50% de los datos están por debajo de la mediana y el 50% están por encima.
#' Cuartiles (Q1, Q2, Q3):

#' Los cuartiles dividen los datos en cuatro partes iguales. Q1 es el percentil 25, Q2 es el percentil 50 (mediana) y Q3 es el percentil 75.
#' Deciles (D1, D2, ..., D9):

#'Los deciles dividen los datos en diez partes iguales.
#'Percentiles más Altos (P90, P95, P99, etc.):

#'Indican el valor por debajo del cual se encuentra el 90%, 95%, 99%, etc., de los datos

#c Se puede usar el metodo perecentile() de numpy para encontrarlo en un dataset

import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages,50)

print(x)