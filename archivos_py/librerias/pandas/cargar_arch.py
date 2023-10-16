
#'                CARGAR ARCHIVOS EN UN DATAFRAME

#' Si los datos con los que se quiere trabajar estan en un archivo, pandas puede cargarlos en una Dataframe

#c Cargar un archivo CSV (Separado por comas):

import pandas as pd

#' Se deve dar la ruta del archivo ya creado
#? Si no existe se pude crear simplemente dandole la terminación csv

# df = pd.read_csv('C:/Users/mar_amez/Desktop/gio/archivos_py/mi_archivo.csv')

# print(df.to_string()) #* to_string() es para devlover el archivo csv completo

# #' La siguiente sentencia permite modificar la cantidad de lineas que se mostraran ocultando las intermedias

# print(pd.options.display.max_rows) #* Numero de filas maximas devueltas (60)

#c Se puede cambiar el numero maximo de filas con la misma sentencia:

pd.options.display.max_rows = 4

df = pd.read_csv('C:/Users/mar_amez/Desktop/gio/archivos_py/librerias/pandas/archivos_csv/tesla.csv')
print(df)