
#' ARBOLES KD (K-DIMENCIONAL)

#'Son estructuras de datos optimizadas para realizar consultas de vecino mas cercano. Estan diseñadas para trabajar
#' mas eficientemente con conjuntos de puntos en espacios de multiples dimenciones

#' La principal ventaja de estos son sus consultas eficientes sobre el punto mas cercano a un punto en un conjunto
#' de puntos.Es util en algoritmos de busqueda en geometria computacional

#' El metodo KDTree() se utiliza para crear un objeto que reprecenta la estructura de arbol KD
#' organiza los puntos en el espacio.

#' query() se utiliza para realizar consultas sobre el árbol KD. Cuando realizas una consulta, obtienes
#' la distancia al vecino más cercano y la ubicación de ese vecino.

#c Encontrar el vecino mas cercano a el punto (1,1):

from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points) #* Construimos un arbol con los puntos y los organizara eficientemente para consultas rapidas

res = kdtree.query((1, 1))#*Estamos realizando una consulta en el árbol KD para encontrar el vecino más cercano
#* al punto (1, 1).query() devuelve un objeto que contiene información sobre la distancia al vecino más cercano y la ubicación del vecino.

#? 2.0: Es la distancia al vecino más cercano desde el punto (1, 1).
#? 0: Es el índice del vecino más cercano en la lista original de puntos.

# print(res)


#' MATRIZ DE DISTANCIA

#' Hay muchas metricas de distancia usadas para encontrar varios tipos de distancias entre dos puntos en ciencia de datos
#' Distancia euclidiana,Distancia coseno, etc.
#' La distnacia entre dos vectores no solo puede ser la longitud de la linea si no tambien el angulo entre ellos
#' con respecto al origen,o el numero de pasos unitarios requeridos

#' Muchos de los algoritmos de machine larning depende en gran medidad de la matriz distancia (vecino mas cercano)

#' DISTANCIA EUCLIDIANA

#c Encuentre la distancia euclidiana entre los puntos dados:

from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)
res = euclidean(p1, p2) #* Encuentra la distancia geometrica entre los dos puntos
# print(res)

#' La Cityblock Distance, también conocida como Manhattan Distance, es una medida de distancia que se calcula
#' considerando solo movimientos en direcciones perpendiculares, similar a cómo te moverías por las calles de una
#' ciudad con bloques cuadriculados (de ahí el nombre Manhattan Distance). En este contexto, solo se permiten
#' movimientos en direcciones vertical u horizontal, no en diagonal.

#' Dados dos puntos (x1,y1) y (x2,y2) la distancia de Manhatan esta dada por la suma de kas diferencias absolutas
#' abs(x2 - x1) + abs(y2 - y1)

#' Tiene aplicación en: Procesamiento de Imágenes: En el análisis de imágenes, especialmente en segmentación y detección de bordes

#c Encontrar la distancia Cityblock:

from scipy.spatial.distance import cityblock

p1 = (1, 0)
p2 = (10, 2)
res_0 = cityblock(p1, p2)#* Da solo la suma total de unidades avanzadas horizonatal y verticalmente
# print(res_0)

#' DISTANCIA COSENO

#' Es el valor del coseno del angulo entre los dos puntos

#c Encuentre lo distancia coseno entre los siguientes puntos :

from scipy.spatial.distance import cosine

res_1 = cosine(p1, p2)

# print(res_1)

#' DISTANCIA DE HAMIMING

#' Es la proporcion de bits donde los dos bits son diferentes
#' Es una forma de medir la distancia de secuencias binarias

#c Encuentre la distancia de hamming entre los siguientes puntos:

from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res_2 = hamming(p1, p2)

print(res_2)