
#' Los graficos son estructuras de datos escenciales

#' SciPy nos da el modulo scipy.sparse.csgraph para trabajar con dichas estructuras de datos

#' Matriz Adyacente

#' Es una matriz n*n donde n es el numero de elementos del grafico
#' Y los valores representan la conexion entre los elementos

#c Cargar una imagen desde el archivo:

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# variable = cv2.imread("C:/Users/mar_amez/Desktop/gio/trabajo_ingenieria/proyecto_HCD/Captura de pantalla (128).png")
# cv2.imshow('Matriz de adjacencia',variable)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#'Para una gráfica como esta, con los elementos A, B y C, las conexiones son:

#' A y B están conectados con el peso 1.

#' A y C están conectados con el peso 2.

#' C y B no están conectados.

#' La Matriz de Adjencia se vería así:

#c      ABC
#c   A:[0 1 2] : conecta con B por medio de 1, conecta con A por medio de 2
#c   B:[1 0 0] : conecta con A por medio de 1
#c   C:[2 0 0] : conecta con A por medio de 2

#' METODOS PARA TRABAJAR CON MATRICES DE ADYACENCIA

#' Componentes conectados: Se puede encontrar todos los componentes conectados con el metodo connect_components()

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

# print(connected_components(newarr)) #* Devuelve una tupla que consiste en dos elementos:

#* Número de componentes conectados: Indica cuántos componentes conectados hay en el grafo.
#* Etiquetas de componente conectado: Una matriz NumPy que asigna una etiqueta a cada nodo, indicando a qué
#* componente conectado pertenece.

#' El metodo Dijkstra el camino mas corto en un grafo de un elemento a otro
#' Este toma los siguientes argumentos

#a 1. return_predecessors : Booleano (verdadero para devolver el camino recorrido completo)
#a 2. indices : Indices para devolver todas las rutas de ese unico elemento
#a 3. limit : Peso maximo del camino

#c Encontrar la ruta mas corta del desde el elemento 1 al 2:

from scipy.sparse.csgraph import dijkstra

print(dijkstra(newarr, return_predecessors=True, indices=0))