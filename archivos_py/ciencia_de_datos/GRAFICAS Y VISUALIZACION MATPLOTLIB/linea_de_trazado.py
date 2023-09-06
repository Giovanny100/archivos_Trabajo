'''
GRAFICA LINEAL

MATPLOTLIB ADMITE LA CREACION DE DIFERENTES TIPOS DE GRAFICAS.
EMPECEMOS POR LA MAS BASICA (GRAFICA LINEAL).

UTILIZAREMOS LOS DATOS DE COVID-19 DEL MODULO ANTERIOR PARA CREAR NUESTRAS GRAFICAS.

MOSTRAREMOS EL NUMERO DE CASOS EN EL MES DE DICIEMBRE.

PARA CREAR UNA GRAFICA LINEAL SIMPLEMENTE TENEMOS QUE LLAMAR LA FUNCION plot() EN NUESTRO DATAFRAME, QUE CONTIENE LOS DATOS CORRESPONDIENTES:
'''

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

#GRAFICAMOS:
#Para lograr ver la figura fue necesario agregar (plt.savefig(nombreopcionaldelgrafico.png)) para que se guarde en nuestra memoria.
import matplotlib.pyplot as plt
plt.xlabel('Day')
plt.ylabel('# Cases')
df[df['month'] == 2]['cases'].plot()
plt.savefig('plotlinal.png')
'''
TAMBIEN PODEMOS INCLUIR VARIAS LINEAS EN NUESTRA GRAFICA.

POR EJEMPLO INCLUYAMOS TAMBIEN LA COLUMNA deaths EN NUESTRO DATAFRAME.
'''

df[df['month'] == 1][['cases','deaths']].plot()
plt.savefig('plotlinal2.png')