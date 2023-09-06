'''
ESTAS TRABAJNDO CON EL CONJUNTO DE DATOS COVID PARA CALIFORNIA QUE INCLUYE EL NUMERO DE CASOS Y MUERTES PARA CADA DIA DE 2020.

ENCUENTRA EL DIA EN QUE LA PROPORCION DE MUERTES /CASOS FUE MAYOR.

PARA ELLO PRIMERO HAY QUE CALCULAR EL RATIO DE MUERTES /CASOS Y AÑADIRLO COMO COLUMNA AL DATAFRAME CON EL NOMBRE 'ratio' Y LUEGO ENCUENTRA LA FILA CORRESPONDIENTE
AL VALOR MAS GRANDE.

IMPORTANTE: LA SALIDA DEBE SER UN DATAFRAME, QUE CONTENGA TODAS LAS COLUMNAS DEL CONJUNTO DE DATOS DE LA FILA CORRESPONDIENTE.
'''
import csv

#Importamos pandas para crear e dataframe:
import pandas as pd

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

df['month'] = pd.to_datetime(df['date'],format = "%d.%m.%y").dt.month_name()

df.drop('state', axis = 1, inplace = True)
df.set_index('date',inplace = True)

#Aqui va nuestro codigo:

#Agregamos al df la columna ratio que es las muertes entre los casos:
df['ratio'] = df['deaths'] / df['cases']

#Encontramos la fila con el valor corespondiente mas grande:
print(df[df['ratio'] == df['ratio'].max()])
