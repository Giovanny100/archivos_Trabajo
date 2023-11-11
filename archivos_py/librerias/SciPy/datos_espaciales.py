
#' Los datos espaciales se refiren a datos que son representados en un espacio geomatrico

#'Scipy tiene el modulo scipy.spatial() para trabajar con datos espaciales

#' TRIANGULACIÓN

#? Método que se utiliza para dividir un poligono en triangulos con los que se puede calcular el área del poligono

#' Una triangulación con superficies significa crear superficies compuestas de triangulos
#' en los que todos los puntos dados están en al menos un vértice de cualquier triángulo en la superficie.

#' Un método para generar estas triangulaciones a través de puntos es la Delaunay() Triangulación.

#c Cree una triangulación a partir de los siguientes puntos:

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

#' La siguiente matriz son cordenadas en el plano (x,y):

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

#' Se realiza la triangulación:

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices) #* matriz 2*5
plt.scatter(points[:, 0], points[:, 1], color='r') #* matriz de grafos

plt.show()

#' Envolvente convexo: Es el más pequeño de los poloigonos que toma todos los puntos
#' Se puede usar el metodo ConvexHull() para crear un envolvente convexo

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# Crear un envolvente convexo de los siguientes puntos:

#* Se definen los puntos que se graficaran en el plano 2D en una matriz:
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

#* La funcion ConvexHull es para calcular el envolvente convexo:
hull = ConvexHull(points)

#*Se ocupa la propiedad simplices de la instancio convexhull que nos da los indices de los vertices que forman caras:
hull_points = hull.simplices

#* scatter es para visualizar los puntos originales en el gráfico:
plt.scatter(points[:,0], points[:,1]) #? [:,0] Toma todas las filas de la columa x y [:,1] de y

for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

#? points[simplex,0]: Aquí estamos accediendo a las coordenadas x de los puntos que forman una cara (simplex)
#?de la envolvente convexa

#? simplex contiene los índices de los vértices que forman una cara de la envolvente convexo

#?points[simplex,0] toma todas las filas de la matriz points correspondientes a esos índices y extrae las
#? coordenadas x.

#? 'k-': Este argumento es una cadena que especifica el estilo de la línea en el gráfico. En este caso,
#? 'k-' significa una línea negra sólida ('k' representa negro y '-' representa una línea sólida).

plt.show()