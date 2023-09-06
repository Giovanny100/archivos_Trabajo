'''
CREAREMOS UN ARCHIVO CSV
'''

#Importamos csv para crear el archivo y escribir en el:
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

#Creamos el Dataframe para los datos del archivo csv de datos covid:
df = pd.DataFrame(casos)

#Especificamos indices personalizados para el dataframe:
df_indices = pd.DataFrame(casos, columns = ['date','state','cases','deaths']) #columns es para modificar los nombres de las columnas

print(df_indices)

#Pasar el dataframe a archivo excel:
#Podemos solo escribir el nombre del mismo dataframe para que se nos genere el archivo automaticamente en donde estamos trabajando.
#Hay que conciderar que el archvo creado en python no se vaa poder leer y hay que salir a la ventana de microsoft excel para poder ver el archivo.
#Tambien hay que tener en cuenta que el archivo creado tendra los indices por default que pandas le da al dataframe.
df_indices.to_excel('covid-19.xlsx')

#Quitar los indices por defalt del dataframe para exportarlo a archivo excel:
df_indices.to_excel('covid-19_noind.xlsx',index=False)

