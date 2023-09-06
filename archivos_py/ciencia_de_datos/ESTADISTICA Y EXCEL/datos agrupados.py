import random
import numpy as np
import pandas as pd
#Pedir datos al usuario:

n = int(input('Ingrese el tamaño de la muestra:\r\n'))

lim_inf = int(input('Ingrese Limite inferior de los datos:\r\n'))

lim_sup = int(input('Ingrese Limite inferior de los datos:\r\n'))

#Lista donde se almacenaran los datos aleatorios con los parametros proporcionados
datos  = []

#Codigo para tomar los datos aleatorios hasta que se junte el tamaño de la muestra que queremos:
while len(datos) < n:
    dato = random.randint(lim_inf,lim_sup)
    datos.append(dato)

#Exportar los datos a excel:

col1 = "NIVELES DE GLUCOSA EN SANGRE"

data = pd.DataFrame({col1:datos})
data.to_excel('estadisticas de glucosa.xlsx', sheet_name='sheet1', index=False)

#MEDIDAS DE TENDENCIA CENTRAL:

MEDIA = sum(datos)/len(datos)
print(MEDIA)

datos_var = []
for dato in datos:
    xi = pow(dato-MEDIA,2)
    datos_var.append(xi)
VARIANZA = sum(datos_var)/(len(datos)-1)
print(VARIANZA)

DESVIACION = np.sqrt(VARIANZA)
print(DESVIACION)






