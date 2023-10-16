
#' ELIMINAR DATOS DUPLICADOS

#' Las filas duplicadas son filas que se han registrado mas de una vez

#' duplicated(): Descubrir duplicados, devuelve valores booleanos para cada fila. True (para filas duplicadas)

import pandas as pd

df = pd.DataFrame('C:/Users/mar_amez/Desktop/gio/archivos_py/librerias/pandas/archivos_csv/tesla.csv')

print(df)

print(df.duplicated())