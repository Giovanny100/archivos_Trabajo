'''
Para hacer un ejemplo real podemos importar datos de yahoo finance.

1. Buscar la compañia con su Ticker correspondiente, ejemplo: Para apple es 'APPL'
2. Ir a datos historicos (los datos que se dan son a un periodo de tiempo de una año por default)
3. Click en download (parte superior derecha de la tabla)
4. Por defecto el archivo se descarga como csv
5. Cambiar la ubiacion del archivo a una carpeta para teneer su direccion y poder importarlo a python
6. Para acceder a nuestros datos podemos crear una vaiable donde llamemos a la misma
7.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m
import seaborn as sns

acciones = pd.read_csv("C:/Users/mar_amez/Downloads/TSLA.csv")

# print(acciones) #Genera el dataframe de los datos importados de yahoo

#Si lo que queremos es solo el precio de cierre de la accion:

# print(acciones['Close'])

#Para graficar los datos:

# plt.plot(Apple_acciones['Close'])
# plt.show()

#Pandas prmite saber cuanto han cambiado los valores de la accion con respecto a otro con la funcion shift():

diferencias = acciones['Close'] - acciones['Close'].shift()

# print(diferencias)

# plt.plot(diferencias)
# plt.show()

# Podemos sacar la media y desviacion estandar de las diferencias para analizar si me conviene invertir o no en ellas
# La media me va a decir si es mas comun que pierda o que gane ya que si me da un valor negativo significa que hay perdidas
# La desviacion estandar indica cuan volatil o en que medida crece o decrece del valor inicial de inversion


media = diferencias.mean()
desviacion_estandar = diferencias.std()

print(f'La media de la accion es de  {media} y su desviacion estandar es {desviacion_estandar}')

# Ahora podemos hacer un muestreo de los datos para sacar estadisticas con diferentes datos:
# son datos distintos debido a que se esta usando la funcion random.
mod1 = np.random.normal(media, desviacion_estandar,250)
mod2 = np.random.normal(media, desviacion_estandar,250)
mod3 = np.random.normal(media, desviacion_estandar,250)
mod4 = np.random.normal(media, desviacion_estandar,250)
mod5 = np.random.normal(media, desviacion_estandar,250)
mod6 = np.random.normal(media, desviacion_estandar,250)
mod7 = np.random.normal(media, desviacion_estandar,250)
mod8 = np.random.normal(media, desviacion_estandar,250)
mod9 = np.random.normal(media, desviacion_estandar,250)
mod10 = np.random.normal(media, desviacion_estandar,250)
mod11 = np.random.normal(media, desviacion_estandar,250)
mod12 = np.random.normal(media, desviacion_estandar,250)
mod13 = np.random.normal(media, desviacion_estandar,250)
mod14 = np.random.normal(media, desviacion_estandar,250)

#Creando los modelos para cada muestra:

modelo1 = acciones['Close'][0] + mod1.cumsum()
modelo2 = acciones['Close'][0] + mod2.cumsum()
modelo3 = acciones['Close'][0] + mod3.cumsum()
modelo4 = acciones['Close'][0] + mod4.cumsum()
modelo5 = acciones['Close'][0] + mod5.cumsum()
modelo6 = acciones['Close'][0] + mod6.cumsum()
modelo7 = acciones['Close'][0] + mod7.cumsum()
modelo8 = acciones['Close'][0] + mod8.cumsum()
modelo9 = acciones['Close'][0] + mod9.cumsum()
modelo10 = acciones['Close'][0] + mod10.cumsum()
modelo11 = acciones['Close'][0] + mod11.cumsum()
modelo12 = acciones['Close'][0] + mod12.cumsum()
modelo13 = acciones['Close'][0] + mod13.cumsum()
modelo14 = acciones['Close'][0] + mod14.cumsum()


#Generar el grafico de comparacion:

plt.figure(figsize=(11,7))
plt.title('Price prediction')
plt.xlabel('Tiempo')
plt.ylabel('Precio')

plt.plot(acciones['Close'],label ='Trayectoria real', color = 'gray', linewidth = 3)
plt.plot(modelo1, label = 'Modelo 1', color = 'pink')
plt.plot(modelo2, label = 'Modelo 2', color = 'mediumvioletred')
plt.plot(modelo3, label = 'Modelo 3', color = 'violet')
plt.plot(modelo4, label = 'Modelo 4', color = 'magenta')
plt.plot(modelo5, label = 'Modelo 5', color = 'deeppink')
plt.plot(modelo6, label = 'Modelo 6', color = 'green')
plt.plot(modelo7, label = 'Modelo 7',color = 'yellow')
plt.plot(modelo8, label = 'Modelo 8',color  = 'blue')
plt.plot(modelo9, label = 'Modelo 9',color = 'red')
plt.plot(modelo10, label = 'Modelo 10',color = 'gold')
plt.plot(modelo11, label = 'Modelo 11',color = 'black')
plt.plot(modelo12, label = 'Modelo 12',color = 'orange')


plt.legend()
plt.show()

'''
CONCLUCIÓN: PARA HACER ESTIMACIONES CON ALTA PRESICION LO QUE SE HACE ES HACER VARIAS PREDICCIONES ALEATORIAS DE TAL FORMA QUE LAS MISMAS ASEGUREN UN RANGO
O INTERVALO EN EL QUE HAY ALTA POSIBILIDAD DE QUE CAIGA MI ACCION, ESTO ES LO QUE SE CONOCE COMO INTERVALO DE CONFIANZA.
'''

#into the database it will to find the most recent update and then update saved data