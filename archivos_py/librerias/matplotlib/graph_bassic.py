
#' Para crear una linea de puntos desde la posicion (x1,y1) a la posición (x2,y2), se puden usar matrices numpy

import matplotlib.pyplot as plt
import numpy as np

# x= np.array([0,6])
# y = np.array([0,256])

#' Por defecto se traza una linea recta que es el vector del P1 a P2:

# plt.plot(x, y) #* plt.plot(absisas, ordenadas)
# plt.show()

#' Si solo se requiere graficasr los puntos sin la linea se usa el argumento corto: 'o' que significa rings

# plt.plot(x,y,'o')
# plt.show()

#'Se puede graficar varios puntos como se quiera. Asegurarse de que se tiene la misma cantidad de puntos en ambos ejes

#c Dibujar una linea de la posición (1,3) a (2,8) luego (6,1) y finalmente a (8,10):

# x = np.array([1,2,6,8])
# y = np.array([3,8,1,10])

# plt.plot(x, y)
# plt.show()

