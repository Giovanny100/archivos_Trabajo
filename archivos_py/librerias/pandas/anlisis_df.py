
#' ANALISIS DE DATAFRAMES

#' VISUALIZACION DE DATOS
#' Uno de los metodos mas usados para obtener una descripcion genral rapida del dataframe es head()

#' head() Devuelve los encabezados y un numero especifico de filas comenzando desde arriba

#c Obtenga una descripción general rápida imprimiendo las primeras 10 filas del DataFrame:

import pandas as pd

df = pd.read_csv('C:/Users/mar_amez/Desktop/gio/archivos_py/mi_archivo.csv')
# print(df.head(1)) #* Devuelve solo una fila del dataframe con el encabezado de los datos

#' Tambien esta el metodo tail() para devolver el encabezado y numero de filas comenzando desde abajo

# print(df.tail(1)) #* Devuelve la ultima fila del dataframe

#' Información sobre los datos

#' Los objetos Dataframes tienen un metodo llamado info(), que da informacion sobre el conjunto de datos

print(df.info())