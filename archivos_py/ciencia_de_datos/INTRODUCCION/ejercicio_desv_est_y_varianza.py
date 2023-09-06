'''
UTILIZANDO EL MISMO CONJUNTO DE DATOS DE VACUNACIONES CALCULA Y GENERA LA VARIANZA.
DECLARA UNA LISTA DE DATOS Y UTILIZA UN BUCLE PARA CALCULAR EL VALOR.
PRONTO CONOCEREMOS FORMAS MAS SENCILLAS DE CALCULAR LA VARIANZA Y OTRAS ESTADISTICAS.
'''
from statistics import mean

vacunas_recibidas = [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3]
media = mean(vacunas_recibidas)

#Codigo para calcular la varianza de una lista de datos:

diferencia_de_cuadrados = []
for i in vacunas_recibidas:
    diferencia_de_cuadrados.append(pow(i - media,2))
varianza = sum(diferencia_de_cuadrados)/len(vacunas_recibidas)
print(varianza)


#OTRA FORMA DE HACERLO ES IMPORTANDO numpy:

import numpy as np

a = np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3])

media2 = np.sum(a)/a.size
var = np.sum((a - media2)**2)/a.size
print(var)