
#' OPTIMIZADORES DE SCIPY

#' Son conjuntos de procesos definidosen scipy que encuentran el valor minimo de una función o la raiz de una ecuación

#c Optimización de funciones

#' Escencialmente todos los algoritmos en machin learning no son mas que ecuacón compleja que necesita ser minimizada
#' con ayuda de los datos

#c Raiz de una ecuación

#' Numpy puede encontrar la raiz de una ecuacion lineal o polinomica (algebraicas) pero tendra dificultades para
#' resolver funciones trasendentes (no algebraicas)

#' Ejemplo: x + cos(x) ; se puede usar la funcion optimize.root de SciPy
#' Esta función toma dos argumentos:

#a fun : una función que representa la ecuación
#a x0 : una estimación inicial de la raiz

#' La función devueve un objeto con informacion de la solución
#' La solución se da en el atributo x del objeto

from scipy.optimize import root
from math import cos

def fun(x):
    return x + cos(x)

myroot = root(fun,0) #* Devuelve un valor aproximado de la raiz
# print(myroot.x)
# print(myroot) #* Devuelve toda la informacion sobre la solución

#' A continuación se da una descripción de todos los datos que se devuelven:

#? [-0.73908513] : Solucion aproximada dela función
#? fjac: array([[-1.]]) : Matriz jacobiana delas derivadas parciales de las funciones (para este caso solo -1)
#? fun: array([0.]) : Valor de la función evaluada en la raíz encontrada
#? message: 'The solution converged.' : Cumple los criterios de convergencia
#? nfev: 9: Numero de veces que se evaluó la función
#? qtf: array([-2.66786593e-13]) : Dirección de busqueda (vector que indica la direccion de movimiento de la sol.)
#? r: array([-1.67361202]) : Factor de descomposición QR del sistema lineal
#? status: 1 : Estado de la optimización (indica que se ha encontrado una solución)
#? success: True : El booleano indica si la optimización fue exitosa
#? x: array([-0.73908513]) valor de x encontrada

#' MINIMIZANDO UNA FUNCIÓN

#' Una función en este contexto representa una curva (tiene maximos y minimos)
#' El punto más alto de toda la curva es llamado maximo global y el resto maximos locales
#' El punto más bajo de la curva es llamado minimo global y el resto minimos locales

#' Podemos usar la función scipy.optimizeminimize() la cual toma los siguientes argumentos:

#a fun : una represntación de la ecuación
#a xo : suposición inicial de la raíz
#a x0 : Nombre del metodo a utilizar. Valores validos:

#c MÉTODOS:

#c 'CG'
#c 'BFGS'
#c 'Newton-CG'
#c 'L-BFGS-B'
#c 'TNC'
#c 'COBYLA'
#c 'SLSQP'

#c Devolución de llamada : función llamada después de cada iteración de optimización.

#c opciones : un diccionario que define parámetros adicionales:

#c {
#c     "disp": boolean - print detailed description
#c     "gtol": number - the tolerance of the error
#c  }

#c Minimiza la función x^2 + x + 2 con BFGS:

from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)