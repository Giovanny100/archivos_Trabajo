import matplotlib.pyplot as plt
import numpy as np

#? Definir una función lambda:

funcion = lambda x: x**3  #* Reemplaza esta función lambda con la que desees graficar

#? Crear un rango de valores x:

x = np.linspace(-4, 4, 50)  #* Rango de -10 a 10 con 100 puntos

#? Calcular los valores correspondientes de y utilizando la función lambda:

y = funcion(x)

#? Crear el gráfico:

plt.figure(figsize = (9, 9))  #* Tamaño de la figura
plt.plot(x, y, label = 'Función Personalizada', color = 'c')  #* Graficar la función
plt.xlabel('Eje X') #* Leyenda del eje y
plt.ylabel('Eje Y') #* Leyer del eje x
plt.title('Gráfico de una Función Lambda')
plt.legend()  #* Agregar leyenda
plt.grid(True)  #* Agregar una cuadrícula al gráfico (opcional)

#? Remarcar los ejes x e y en el origen (0,0):

plt.axhline(5, color='black', linewidth= 1.1)
plt.axvline(0, color='black', linewidth= 1.1)

#? Mostrar el gráfico:

plt.show()
