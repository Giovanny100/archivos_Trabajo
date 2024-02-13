
#' REGRESION LINEAL PARA REDES NEURONALES

#' Librerias:
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

#' Cargar el dataset:

boston = load_boston()
print(boston.DESCR)

#' Crear matriz de entrada X:
#' Convertimos el set de datos a matrices:

X = np.array(boston.data[:,5]) #* Media de habitacions por vivienda
Y = np.array(boston.target) #* Valor media
print(X)
#' Graficar las matrices:

#* El argumento alfa es para darle trasparencia a los puntos
plt.scatter(X, Y, color='blue', alpha = 0.5) #* Grafico de dispercion

#' Creamos columna de unos para termino independiente:
X = np.array([np.ones(506),X]).T

# Con el anterior grafico de dispercion se tratara de ajustar la linea
#C Formula para calcular el error cuadratico medio (MCO): B = (X^T * X)^-1 * X^T * Y

#' Programar la ecuacion de error:
#*Para invertir la matriz se ultiliza: np.linalg.inv
B = np.linalg.inv(X.T @ X) @ X.T @ Y #* Se debe utilizar arroba porque eso da el producto matricial

#'Para hacer la regresion necesitamos los puntos extremos:

plt.plot([4,9],[B[0]+ B[1] * 4 , B[0] + B[1] * 9], c = 'green')
plt.title('Tendencia por sucidios')
plt.grid(True)
plt.show()

