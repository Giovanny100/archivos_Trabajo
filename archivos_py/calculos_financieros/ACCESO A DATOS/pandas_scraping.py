'''
PANDAS PUEDE SER USADA PARA RASPAR Y ALAMACENAR DATOS EN FORMA DE TABLA.
CON LA AYUDA DE PANDAS, EN UN PAR DE LINEAS PODEMOS OBTENER LOS DATOS DECEADOS.

PANDAS TIENE LA FUNCION read_html() LA CUAL ES USADA PARA CONVERTIR TABLAS EN SITIOS WEB A DATAFRAMES.

POR EJEMPLO VAMOS A SCRAPEAR LA LISTA DE LA COMPAÑIA S&P 500 DESDE WIKIPEDIA

LA LISTA ESTA DISPONIBLE EN UN ARTICULO DE LA PAGINA DE WIKIPEDIA COMO UNA TABLA.

NOSOTROS SIMPLEMENTE NECESITAMOS LLAMAR LA FUNCION read_html() CON EL URL DE LA PAGINA COMO EL PARAMETRO.

NOTA: PARA PODER EXPORTAR LOS DATOS COMO UN DATAFRAME ES NECESARIO DESCARGAR EL CONTENIDO lxml DESDE cmd.
'''

import pandas as pd

data = pd.read_html('https://en.m.wikipedia.org/wiki/List_of_S%26P_500_companies')

# Cada tabla en la pagina web es almacenada en un dataframe en un indice separado
#La primer tabla tiene el indice cero y así suscesivamente
# Accedemos y devolvemos la primer tabla

df = data[0]
print(df)

#Ahora vamos a devolver solo las columnas de simbolo y seguridad:

df =df[['Symbol','Security']]
print(df)