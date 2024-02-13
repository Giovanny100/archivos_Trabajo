
#' Podemos agregar un mapa de colores agregando el argumento cmap y agregar el metodo plt.colorbar
#' El argumento s en scatter sirve para cambiar el tamaño de los puntos (Se puede pasar como valor una martiz de tamaños)
#' Argumento alpha para cambiar la transparencia de los puntos

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100]) #* Matriz de colores para los puntos
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75]) #* Matriz de tamaños para los puntos

# plt.scatter(x, y, c=colors, cmap='viridis', s = sizes, alpha=0.55)
# plt.colorbar()
# plt.show()

#' Se puede hacer una combinación de tamaños y colores:

a = np.random.randint(500, size=(100))
b = np.random.randint(10, size=(100))
colors = np.random.randint(20, size=(100))
sizes =7* np.random.randint(100, size=(100))

plt.scatter(a, b, c=colors, s=sizes, alpha=0.7, cmap='nipy_spectral')

plt.colorbar()

plt.show()