'''
ANTES DE TRABAJAR CON DATOS REALES, VAMOS A CREAR PRIMERO UN DATAFRAME MANUALMENTE PARA EXPLORAR SUS FUNCIONES.

LA FORMA MAS FACIL DE CREAR UN DATAFRAME ES CREAR UN DICCIONARIO
'''

data = {

    "ages" : [14,18,24,42],
    "heights" : [165,180,176,184]
}

'''
CADA CLAVE ES UNA COLUMNA, MIENTRAS QUE EL VALOR ES UNA MATRIZ QUE REPRECENTA LOS DATOS DE ESA COLUMNA.

AHORA PODEMOS PASAR ESTE DICCIONARIO AL CONSTRUCTOR DATAFRAME.
'''

import pandas as pd

df = pd.DataFrame(data)

print(df) #imprime una tabla con los valores y claves del diccionario.

'''
MARCOS DE DATOS

EL DATAFRAME CREA AUTOMATICAMENTE UN NUMERO INDICE PARA CADA FILA.

PODEMOS ESPECIFICAR UN INDICE PERSONALIZADO, AL CREAR EL MARCO DE DATOS:
'''

fd = pd.DataFrame(data, index=['james','bob','amy','eric'])

#ahora se puede acceder a una fila utilizando su indice y la funcion loc[]:

print(fd.loc['bob']) #muestra la fila que corresponde al indice bob