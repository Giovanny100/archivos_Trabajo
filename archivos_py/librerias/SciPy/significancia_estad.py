
#' La significacion estadistica se refiere a que el resultado producido tiene una razon detrás, no se produjo por casualidad
#'  SciPy proporciona scipy.stats que tiene funciones para realizar pruebas de significancia estadistica

#' Algunos conceptos estadisticos importantes:

#? Hipotesis estadistica: Suposición inicial sobre un parametro estadistico
#? Hipotesis nula: Esta supone que la observacion no tiene fundamento estadistico para ser cierta
#? Hipotesis alternativa: Supone que la observacion tiene alguna razon para ser cierta y es contraria a la nula

#?One-tailed test: "Prueba de una cola" o "Prueba unidireccional". Esta prueba evalúa si una muestra es
#?significativamente mayor o menor que una cierta referencia, pero no ambos.

#?Two-tailed test: "Prueba de dos colas" o "Prueba bidireccional". Esta prueba evalúa si una muestra es
#?significativamente diferente (mayor o menor) que una cierta referencia, sin especificar la dirección de
#?la diferencia.

#? VALOR ALFA

#? El valor alfa es el nivel de significancia.
#?Qué tan cerca de los extremos deben estar los datos para que se rechace la hipótesis nula.
#?Generalmente se toma como 0,01, 0,05 o 0,1.

#? VALOR P

#?El valor P indica qué tan cerca del extremo están realmente los datos.
#?El valor de p y los valores alfa se comparan para establecer la significación estadística.
#?Si el valor de p <= alfa rechazamos la hipótesis nula y decimos que los datos son estadísticamente significativos
#? en caso contrario aceptamos la hipótesis nula.

#? Prueba T (Prueba de hipotesis):

#? Las pruebas T se utilizan para determinar si existe una diferencia significativa entre las medias de dos
#? variables y nos permiten saber si pertenecen a la misma distribución.

#? Ho (hipotesis nula): Supone que las medias son iguales de ambos conjuntos
#? Ha (hipotesis alternativa): Supone que las medias son diferentes

#? La prueba t calcula un valor t, que indica cuántas desviaciones estándar está la diferencia observada
#? entre las medias respecto a lo que se esperaría por azar.

#' La función ttest_ind() toma dos muestras del mismo tamaño y produce una tupla de estadístico t y valor p.

#c Encuentre si los valores dados v1 y v2 provienen de la misma distribución:

import numpy as np
from scipy.stats import ttest_ind

#* Conjuntos de datos aleatorios de 0 a 100:
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

#* Se realiza una prueba t de independencia (t-test) entre los dos conjuntos de datos v1 y v2.
#* La función ttest_ind devuelve un objeto que contiene estadísticas y p-valores asociados con la prueba t

res = ttest_ind(v1, v2)
# print(res)

#* El valor t (statistic) Indica que la diferencia observada entre las medias, Si es pequeña y no es
#* estadísticamente significativa.

#* El p-valor (pvalue) Es relativamente alto, lo que sugiere que no hay evidencia significativa
#* para rechazar la hipótesis nula. No hay suficiente evidencia para afirmar que las medias son diferentes.

#' Para solo devolver el valor de p (numero de desviaciones estandar lejos de la media) se usa la propiedad pvalue

pv = ttest_ind(v1, v2).pvalue
# print(pv)

#' TEST KS: Analiza si los valores dados siguen una distribucion
#' Toma como parametros el valor a probar y el CDF (puede ser una cadena o una funcion llamable que devuelva la probalilidad)
#' Puede usarse como pruba de una o dos colas aunque de forma predeterminada como dos colas

from scipy.stats import kstest

v = np.random.normal(size = 100)
ks = kstest(v, "norm")
# print(ks)

#' DESCRIPCION ESTADISTICA DE DATOS

#' Para ver un resumen de valores en una matriz se usa la funcion describe()
#'Esto devlovera la siguiente descripcion:

#'Numero de observaciones (nobs)
#'Valores minimos y maximos
#' Media
#' Varianza
#' Curtosis

#c Mostrar la descripcion estadistica de los datos de una mtriz:
from scipy.stats import describe
desc = describe(v)
# print(desc)

#' PRUEBAS DE NORMALIDAD

#' Se basan en la asimetria y kurtosis.La funcion normaltest() devuelve el valor de p para la hipotesis nula
#' X proviene de una distribucion normal

#' ASIMETRIA

#' Una medda de simetria de los datos
#' Para distribuciones normales es 0
#' Si es negativa significa que los datos son asimetricos o estan desviados a la izquierda
#' Si es positiva significa que los datos son asimetricos o estan desviados a la derecha

#' CURTOSIS

#' Es una medida de si los datos estan lijeramente o muy desviados de una distribucion normal
#' Curtosis positiva significa que los datos estan muy desviados de la distribucion normal (cola larga)
#' Curtosis negativa significa que los datos estan lijeramente desviados de la distribucion normal (cola corta)

#c Encontrar la asimetria y curtosis de los valores de la matriz:

from scipy.stats import skew, kurtosis

print(skew(v)) #* El valor representa
print(kurtosis(v))

#c Averiguar si los datos de una matriz vienen de una distribucion normal:

from scipy.stats import normaltest

print(normaltest(v))