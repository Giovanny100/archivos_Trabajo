

#' GREFICANDO DATA FRAMES (PANDAS)

#' Pandas usa el metodo plot() para crear diagramas, usamos el submodulo Pylot para visulizar el diagrama

#c Graficar el siguiente DataFrame:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/mar_amez/Desktop/gio/archivos_py/librerias/pandas/archivos_csv/data.csv')

df.plot() #* Genera el grafico adecuado con base en los datos del DataFrame

plt.show() #* Muestra el grafico ya gtenerado anteriormente

#' GRAFICOS DE DISPERCIÓN

#' Se puede especificar que tipo de gráfico se necesita con el argumento kind
#' Un grafico de disperción de los datos requiere un eje "x" y "y"
#' Para ele ejemplo usaremos "Duración" como eje x y "Calorias" como y. Entonces se pasan como argumentos

df.plot(kind = 'scatter', x = "Duration", y = "Calories") #*Grafico de disperción de "Calorias" vs "Duración"
plt.show()

#! Se puede aprecior que tal como la correlación lo predecia (0.922721), es una buena correlación lo que se aprecia
#! como la tendencia de ser creciente el gráfico

# Crear un diagrama de dispersion en donde haya una mala correlacion de los datos:

df.plot(kind = "scatter", x = "Duration",y = "Maxpulse")
plt.show()

#! Una mala correlación (alejada de 1 o -1) significa que los datos estan muy dispersos y no siguen un patron predecible

