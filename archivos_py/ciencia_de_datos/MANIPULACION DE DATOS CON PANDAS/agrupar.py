'''
AGRUPAR

DADO QUE TENEMOS UNA COLUMNA MONTH PODEMOS VER CUANTOS VALORES TIENE CADA MES, UTILIZANDO LAS FUNCIONES value_counts():
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

df['month'] = pd.to_datetime(df['date'],format = "%d.%m.%y").dt.month_name() #agrea la columna mes en funcion de date especificando el formato.

print(df['month'].value_counts()) #Devuelve el numero de registros del mes.

'''
PODEMOS VER QUE, POR EJEMPLO, ENERO SOLO TIENE 7 REGISTROS, MIENTRAS QUE LOS OTROS MESES TIENEN DATOS PARA TODOS LOS DIAS.

value_counts() DEVUELVE CUANTAS VECES APARECE UN VALOR EN UN CONJUNTO DE DATOS, TAMBIEN LLAMADO FRECUENCIA (FRECUENCY) DE LOS VALORES.

AHORA VAMOS A DETERMINAR EL NUMERO DE INFECCIONES TOTALES DE CADA MES.

PARA ELLO TENEMOS QUE AGRUPAR NUESTROS DATOS POR LA COLUMNA DEL MES Y LUEGO CALCULAR LA SUMA DE LA COLUMNA DE CASOS DE CADA MES
'''

print(df.groupby('month')['cases'].sum()) #La funcion grupby() se utiliza para agrupar nuestro conjunto de datos por la columna dada.

#TAMBIEN PODEMOS CALCULAR EL NUMERO DE CASOS TOTALES EN TOODO EL AÑO:

print(df['cases'].sum()) #Dado que en nuestros datos solo tenemos registros de enero y son solo dos casos solo deveulve 2.

#Del mismo modo podemos utilizar min(), max(),mean(),etc.para encotrar los valores correspondientes de cada grupo.