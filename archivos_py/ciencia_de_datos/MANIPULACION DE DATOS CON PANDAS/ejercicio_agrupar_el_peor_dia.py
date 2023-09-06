'''
DADOS LOS DATOS DE COVID-19, ENCUENTRA EL DIA CON EL MAXIMO DE CASOS EN UN MES DETERMINADO.

TOMA ELO NOMBRE DE UN MES COMO ENTRADA Y GENERA FILA QUE CORRESPONDE LA FILA CON EL MAXIMO NUMERO DE CASOS EN ESTE MES.

PUEDES FILTRAR EL DATAFRAME PARA EN MES EN CUESTION Y, A CONTINUACION, SELECCIONA LA FILA CON EL MAXIMO NUMERO DE CASOS EN ESTE MES.

IMPORTANTE: LA SALIDA DEBE SER UN DATAFRAME, QUE INCLUYE TODAS LAS COLUMNAS.

POR EJEMPLO PARA EL MES DE FEBRERO, EL RESULTADO DE DATOS SERIA:

cases deaths month

date

2020-02-26  15  0  February

EL CODIGO DADO AÑADE UNA COLUMNA MONTH AL CONJUNTO DE DATOS Y AÑA DE UN INDICE.NO CAMBIES ESA PARTE DEL CODIGO.
'''

import pandas as pd

#ESTE CODIGO ES EL QUE HICIMOS APARTE:
import csv

archivo = open("ca-covid.csv", "w")
print("Se ha creado el archivo CSV")

# Lista de datos
casos = [
    ['25.01.20', 'California', 1,0],
    ['26.01.20', 'California', 1,0],
    ['27.01.20', 'California', 0,0],
    ['28.01.20', 'California', 0,0],
    ['29.01.20', 'California', 0,0],
]

# Escritura de datos en el archivo CSV
with open('ca-covid.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(casos)
print("Se ha escrito en el archivo CSV")

# Lectura de datos en el archivo CSV
with open('ca-covid.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
print("Se ha leído el archivo CSV")

#Especificamos indices personalizados para el dataframe:
df = pd.DataFrame(casos, columns = ['date','state','cases','deaths'])

#Agregar columna de mes:
df['month'] = pd.to_datetime(df['date'],format = "%d.%m.%y").dt.month_name()


#ESTE ES EL CODIGO QUE SE AGREGA EN EL EJERCICIO PARA PODER TRABAJAR CON LOS DATOS:

#dorp() deveuelve el mismo dataframe pero elimina la columna especificada, en este caso 'state':
#El parámetro axis especifica la dirección a lo largo de la cual se aplica un determinado método o función en un DataFrame. El axis = 0 representa que la función se
#aplica en forma de columna, y el axis = 1 significa que la función se aplica en forma de fila en el DataFrame.
#Con el parámetro inplace establecido como True , las columnas se eliminan del DataFrame original; de lo contrario, se devuelve una copia del original.
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month_name() #esto ya se habia agregado anteriormente en la linea 55

#se puede utilizar para establecer matrices o columnas de longitud apropiada como índice del DataFrame incluso después de la creación del DataFrame. El nuevo índice
#establecido puede reemplazar al índice existente o también puede ser expandido sobre el existente.
df.set_index('date', inplace=True) #agrego la columna data.

#Pedimios entrada del mes al usuario:
month_user = input()
#Calculamos el maximo de casos del mes.
maxim = df[df["month"]==month_user]['cases'].max()

#Imprimimos los casos:
print(df[df["cases"] == maxim ])
