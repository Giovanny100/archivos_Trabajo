
#'                 FUNCIONES UNIVERSALES

#'Son funciones numpy que operan sobre el objeto array (matriz)
#' Las funciones numpy implementan la vectorizacion en matrices para iterar mucho mas rapido sobre elemetos
#' Proporcionan trnasmicion y metodos adicionales como reducir, acumular, etc. que son utiles para cálculo

#c Argumentos:

#c where : Define sobre que elementos se aplicaran las operacions (Matriz booleana)
#c dtype : Define el tipo de retorno de los elementos
#c out : Matriz de salida donde se deb copiar el valor de retorno

#? VECTROIZACIÓN: Convertir declaraciones iteraticas a una operacion basada en vectores (optimiza los calculos)
#? Las cpu actuales estan optimizadas para estas operaciones.

#' Para crear tu propio ufunc, debes definir una función, como lo haces con las funciones normales en Python
#' luego la agregas a tu biblioteca NumPy ufunc con el frompyfunc()método.

#'El frompyfunc()método toma los siguientes argumentos:

#c function- El nombre de la función.
#c inputs- el número de argumentos de entrada (matrices).
#c outputs- el número de matrices de salida.

#a Creando una ufunc:

import numpy as np

def myadd(x, y):
  return x+ y

myadd = np.frompyfunc(myadd,2,1) #* Aqui estamos agregandola a numpy

# print(myadd([1,2,3,4],[5,6,7,8]))

#a Sin ufunc, podemos usar el método integrado de Python zip():

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
# print(z)

#a NumPy tiene una ufunc para esto, llamada add(x, y) que producirá el mismo resultado:

z = np.add(x, y)

print(z)