# Importamos el modulo csv
import csv

# Crea un archivo CSV y da un mensaje en consola
archivo = open("datos.csv", "w")
print("Se ha creado el archivo CSV")

# Lista de datos
personas = [
    ['Pablo', 'Garcia', 'CDMX'],
    ['Juan', 'Perez', 'MORELOS'],
    ['Maria', 'Garcia', 'TIJUANA'],
]


# Escritura de datos en el archivo CSV
with open('datos.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(personas)
print("Se ha escrito en el archivo CSV")


# Lectura de datos en el archivo CSV
with open('datos.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
print("Se ha leído el archivo CSV")

