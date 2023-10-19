
#' CORRELACIÓN DE DATOS

#' Pandas tiene el método corr() que calcula la relación entre cada columa de tu conjunto de datos

#? El resultado de la correlación es una tabla con muchos datos que representan que tan buena es la relación
#? entre las dos columnas de datos

#? El numero varia de -1 a 1

#? 1 (significa que hay una relación uno a uno); Relación perfecta

#? 0.9 Es tambien una buena correlación y si se incrementa un valor probablemente el otro lo haga igual

#? -0.9 Seria una realción tan buena como 0.9 pero si incrementa el valor el otro probablemente disminuya

#? 0.2 No seria una buena relación, es decir que si un valor aumenta no necesariamente el otro tambien lo haga

import pandas as pd

arch = pd.read_csv('C:/Users/mar_amez/Desktop/gio/archivos_py/librerias/pandas/archivos_csv/data.csv')

df = pd.DataFrame(arch)

print(df.corr()) #* Devuelve la correlacion de cada columna ignorando las no numéricas

#' Analizaremos las correlaciones para los datos de nuestro archivo csv

#' Correlación perfecta: En la matriz de "Duracion", "Duracion" (1)
#'Buena correlación: En la matriz de "Duracion", "Calorias" se obtiene 0.922721
#' Mala correlación: En la matriz de "Duracion", "Maxpulse" se obtiene 0.009403

