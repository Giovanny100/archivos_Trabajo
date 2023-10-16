
#' LEER ARCHIVOS JSON EN PANDAS

#' Los grandes conjuntos de datos son a menudo almacenados o extridos como JSON
#' JSON: Es un texto plano pero tiene el formato de un objeto y es de utilidad en el mundo de la programación
#' Un archivo en json es el equivalente a un diccionario en python

import pandas as pd

df = pd.read_json('C:/Users/mar_amez/Desktop/gio/archivos_py/librerias/pandas/arch_JSON/nuevo.json')
print(df.to_string())