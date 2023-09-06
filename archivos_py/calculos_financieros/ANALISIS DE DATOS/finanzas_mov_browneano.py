import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m

#Seaborn permite hacer graficos sofisticados de visualización, esta basada en matplotlib, es sencillo de utilizar para anilisis de datos:
import seaborn as sns

#Con la funcion ''Normal'podemos crear un arreglo de n datos y darle los datos de dispercion estadisticos (Media,Desviacion estandar, Numero de datos)

muestreo_aleatorio = np.random.normal(0,1,10)
print(muestreo_aleatorio)

#Podemnos conciderar el arregro anterior como la variacion de valor de una accion donde la volatilidad es la desviacion estandar:

print(muestreo_aleatorio.mean()) #Media de los datos aleatorios
print(muestreo_aleatorio.cumsum()) #Suma acumulada diaria

#Si tomamos un valor inicial de la accion:
v_ini = 20 #Dolares

#Podemos hacer un arreglo del valor de la accion en cada dia sumando al valor inicial de la accion cada valor de la variacion acumulada:

precio_diario = v_ini + muestreo_aleatorio.cumsum()
print(precio_diario)

#Ahora tambien podemos determinar cuanto subio de la accion en el intervalo de tiempo analizado:

diferencia_precio = precio_diario[9] - precio_diario[0]
print(diferencia_precio)

plt.plot(precio_diario) #Grafico de precio diario de la accion

plt.show()
