
#' HISTOGRAMA

#' Podemos especificar kind = "hist" para crear un histograma
#' Un histograma solo necesita una columna
#' Un histograma nos muestra la frecuencia de cada intervalo ¿Cuantos entrenamientos duraron entre 50 y 60 minutos?
#' Para ele ejemplo usamos "Duration" como columna para crear el histograma

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/mar_amez/Desktop/gio/archivos_py/librerias/pandas/archivos_csv/data.csv')

df['Duration'].plot(kind = 'hist') #* Crea un histograma de frecuancia de la columa "Duration"

plt.show()