
#'                         DISTRIBUCION DE DATOS ALEATORIA

#' Distribución de datos es una lista de valores posibles y la frecuencia de ocurrencia de cada uno de ellos
#' Estas listas son utiles cuando se trabaja con estadisticas y ciencia de datos
#' El modulo random ofrece metodos qie devuelven distribución de datos generada aleatoriamente

#' Una distribución de datos aleatoria es un conjunto de numeros que siguen una determinada funcion de densidad

#? Funcion Densidad de Probabilidad: Describe una probabilidad continua, es decir la probabilidad de todos los
#? valores de una metriz

#' Podemos generarnumeros aleatorios basados en probabilidades definidas usando choise()

#' La probabilidad se establece mediante un numero entre 0 y 1 donde 0 (no ocurrencia) y 1 (siempre ocurrira)
import numpy as np
from numpy import random

#c Generar a partir de la matriz datos aleatorios dando la probabilidades de ocurrencia y especificando 100 datos:

x = random.choice([0, 1, 2, 3], p =[0.2,0.3,0.3,0.2],size = (100))

# print(x)

#' Devolver matrices de cualquier forma y tamaño especificando la forma en el parámetro size(fila,columna).

g = random.choice([0, 1, 2, 3], p =[0.2,0.3,0.3,0.2],size = (3,5))

# print(g)



