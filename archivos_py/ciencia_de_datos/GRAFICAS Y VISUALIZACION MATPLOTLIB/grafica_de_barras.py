'''
LA FUNCION plot() PUEDE TOMAR UN ARGUMENTO KIND, ESPECIFICANDO EL TIPO DE GRAFICA QUE QUEREMOS PRODUCIR.

PARA UNA GRAFICA DE BARRAS, PROPORCIONA kind = 'bar'.

PARA HACER UNA GRAFICA DE BARRAS PARA EL CASO DE INFECCIONES MENSUALES, PRIMERO DEBERIAMOS AGRUPAR LOS DATOS POR LA COLUMNA MONTH, Y LUEGO CALCULAMOS EL NUEMRO DE
CATOS DE ES MES.
'''
import matplotlib.pyplot as plt

import csv

#Importamos pandas para crear e dataframe:
import pandas as pd

archivo = open("ca-covid.csv", "w")
print("Se ha creado el archivo CSV")

# Lista de datos
casos = [
    ['25.01.20', 'Mexico', 1,0],
    ['26.01.20', 'Mexico', 1,0],
    ['27.01.20', 'Mexico', 0,3],
    ['28.01.20', 'Mexico', 1,0],
    ['29.01.20', 'Mexico', 0,8],
    ['01.02.20', 'Mexico', 12,4],
    ['02.02.20', 'Mexico', 1,3],
    ['04.02.20', 'Mexico', 0,0],
    ['27.02.20', 'Mexico', 6,0],
    ['01.03.20', 'Mexico', 1,5],
    ['01.03.20', 'Mexico', 2,1],
    ['01.03.20', 'Mexico', 7,2],
    ['01.04.20', 'Mexico', 5,2],
    ['01.05.20', 'Mexico', 5,1],
    ['01.05.20', 'Mexico', 0,0],
    ['01.06.20', 'Mexico', 23,12],
    ['01.07.20', 'Mexico', 1,0],
    ['01.07.20', 'Mexico', 3,2],
    ['01.08.20', 'Mexico', 4,3],
    ['01.09.20', 'Mexico', 45,23],
    ['01.10.20', 'Mexico', 15,4],
    ['01.11.20', 'Mexico', 56,42],
    ['01.12.20', 'Mexico', 1,1],
]

# Escritura de datos en el archivo CSV
with open('ca-covid.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(casos)

# Lectura de datos en el archivo CSV
with open('ca-covid.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)

#Especificamos indices personalizados para el dataframe:
df = pd.DataFrame(casos, columns = ['date','state','cases','deaths'])

df['month'] = pd.to_datetime(df['date'],format = "%d.%m.%y").dt.month_name()


#GRAFICO DE BARRAS:

df = df.groupby('month')
df['deaths'].sum().plot(kind = 'bar')

plt.savefig('plot.png')

#Tambien se pueden crear graficas con columnas multiples
#La propiedad stacked puede utilizarse para especificar si las barras deben apilarse unas sobre otras:

#df = df.groupby('month')[['cases','deaths']].sum()

#df.plot(kind = 'bar', stacked = True)