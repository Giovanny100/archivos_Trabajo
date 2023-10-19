
#' ELIMINAR DATOS DUPLICADOS

#' Las filas duplicadas son filas que se han registrado mas de una vez

#' duplicated(): Descubrir duplicados, devuelve valores booleanos para cada fila. True (para filas duplicadas)

import pandas as pd

arch = pd.read_csv('C:/Users/mar_amez/Desktop/gio/archivos_py/librerias/pandas/archivos_csv/tesla.csv')

pd.options.display.max_rows = 250

df = pd.DataFrame(arch)

# print(df)

# print(df.duplicated()) #* Devuelve una matriz booleana de las filas repetidas con True

#' Eliminar todos los datos duplicados:

df.drop_duplicates(inplace = True) #* Elimina los datos repetidos (elimino 16 y 17)
print(df.duplicated())

