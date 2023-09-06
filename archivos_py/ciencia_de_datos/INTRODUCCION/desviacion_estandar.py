'''
LA DESVIACION ESTANDAR ES UNA MEDIDA DE DISPERSION DE NUESTROS DATOS.

PARA CALCULARLO, PRIMERO TENEMOS QUE CALR UN VALOR LLAMADO VARIANZA, QUE ES LA MEDIDA DE LAS DIFERENCIAS AL CUADRADO DE LA mean.

'''
from statistics import mean
#EJEMPLO:

lista =  [14,18,19,24,26,33,42,55,67]

#La  media es 33.1:
media = sum(lista)/len(lista)

#PARA CALCULAR LA VARIANZA, TOMAMOS LA DIFERENCIA ENTRE CADA VALOR Y LA MEDIA, ELEVAR AL CUADRADO Y LUEGO PROMEDIAR EL RESULTADO:
diferencia_de_cuadrados = []
for i in lista:
    diferencia_de_cuadrados.append(pow(i - media,2))
varianza = sum(diferencia_de_cuadrados)/len(lista)
print(varianza)

#PARA CALCULAR LA DESVIACION ESTANDAR DE LOS DATOS SOLO SE TOMA LA RAIZ CUADRADA DE LA VARIANZA:

desv_estandar = pow(varianza,0.5)
print(desv_estandar) #Una desviacion estandar baja indica que los valores tinden a estar cerca de la media del conjunto

#PARA CALCULAR LA DESVIACION ESTANDAR DE LOS DATOS SE PUED UTILIZAR LA FUNCION:

from statistics import pstdev

print(pstdev(lista))