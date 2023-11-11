
#' Los grafos son estructuras de datos escenciales en matematica computacional

#? Grafos: Colección de nodos (vertices) y conexión entre nodos (aristaso bordes)
#?Nodos: Son el quivalente a vertices de una figura geometrica

#? Aristas dirigidas: Hay un inicio y un final (La direccion va en una linea especifica)
#? Aristas no dirigidas: Relación bidireccional (No hay direccion)

#' RECORRIDOS EN GRAFOS

#? Busqueda en profundidad(DFS): Algoritmo para recorrer todos los nodos de un grafico llendo tan lejos como se pueda
#* Identificar ciclos y encontrar componentes conectados

#? Busqueda en amplitud(BFS): En lugar de llegar a lo mas lejos de una rama, explora todos los nodos antes de pasar
#? a la siguiente profundidad
#*Encontrar camino corto,buscar niveles,encontrar tdos ls nodos alcanzables desde un nodo de inicio

#' SciPy nos da el modulo scipy.sparse.csgraph para trabajar con dichas estructuras de datos

#' MATRIZ DE ADYACENCIA

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

# newarr = csr_matrix(arr)

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

# print(dijkstra(newarr, return_predecessors=True, indices=0))

#? La salida del anterior codigo es una tupla de dos elementos (distancias mas cortas,predecesores)

#? INTERPRETACION DE LA SALIDA:

#?La distancia más corta desde el nodo de origen (índice 0) a sí mismo es 0 (esto es parte de la definición de distancia en grafos).
#?La distancia más corta desde el nodo de origen (índice 0) al nodo 1 es 1.
#?La distancia más corta desde el nodo de origen (índice 0) al nodo 2 es 2.

#* (array([0., 1., 2.]), array([-9999, 0, 0]))

#?El predecesor del nodo 1 en el camino más corto desde el nodo de origen es el propio nodo de origen
#?(índice -9999 puede indicar que no hay un predecesor, ya que -9999 podría ser una representación de
#?"ninguno" o "sin predecesor").
#?El predecesor del nodo 2 en el camino más corto desde el nodo de origen es el nodo 0.

#' FLOYD WARSHALL

#'Para encontrar la ruta más corta entre pares de elementos se usa floyd_warshall()

from scipy.sparse.csgraph import bellman_ford

mat = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

# nuevo= csr_matrix(mat)
# print(bellman_ford(nuevo, return_predecessors=True, indices=0))

#' BUSQUEDA A PROFUNDIDAD DE PRIMER ORDEN

#' El metodo depth_first_order() se utiliza para realizar un recorrido en profundidad
#' (DFS, por sus siglas en inglés) en un grafo representado por una matriz dispersa. La DFS es un algoritmo
#' de búsqueda en grafos que explora tan lejos como sea posible por cada rama antes de retroceder.

#' Esta funcion toma como argumentos:
#' El grafo (matriz)
#' El elemento inicial para ir a tráves del gráfo

from scipy.sparse.csgraph import depth_first_order

# g = np.array([
#   [0, 1, 0, 1],
#   [1, 1, 1, 1],
#   [2, 1, 1, 0],
#   [0, 1, 0, 1]
# ])

# newg = csr_matrix(g)

# print(depth_first_order(newg, 1)) #* Tupla con información del recorrido en profundidad

#? El primer elemento de la tupla de salida representa el orden en que fueron visitados los nodos 1->0->3->2
#? La segunda matriz de la tupla representa info sobre los predecesores de arbol DSF

#*El valor -9999 se usa generalmente para indicar que no hay predecesor

#?El predecesor del nodo 0 es el nodo 1.
#?El nodo 1 no tiene predecesor (por eso -9999).
#?El predecesor del nodo 2 es el nodo 1.
#?El predecesor del nodo 3 es el nodo 0.

#' AMPLITUD DE PRIMER ORDEN

#' El metodo breadth_first_order() devuelve un primer recorrido en amplitud desde un nodo
#a Toma dos argumentos:

#a El grafo
#a El elemento inicial desde el cual se atravezara (recorrera) le gráfo

#c Recorra el grafo para la matriz de adyacencia dada:

from scipy.sparse.csgraph import breadth_first_order

h = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

# newh = csr_matrix(h)
# print(breadth_first_order(newh, 1)) #* Devuelve tupla de orden de nodos recorridos y predecesores de recorrido