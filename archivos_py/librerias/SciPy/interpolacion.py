
#' Interpolacion con Scipy

#' Es un metodo para encontrar un punto entre dos dados
#' Ejemplo: entre 1 y 2 se puede encontrar por interpolacion 1.5

#' En machin learning es utilizado cuando se tienen datos faltantes en un conjunto de datos y se obtienen por este metodo
#' A lo anterior se le llama imputación
#' Tambien es utilizado cuando necesitamos suavizar (eliminar ruido) los puntos discretos de un conjunto de datos

#' Scipy tiene un modulo llamado scipy.interpolate que tiene muchas funciones para trabajar con interpolacion

#' Interpolacion en una dimencion (1D)

#' La función interp1d()se utiliza para interpolar una distribución con 1 variable

#c Para xs e ys dados, interpola valores de 2,1, 2,2... a 2,9:

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

#' INTERPOLACION SPLINE

#' En la interpolación 1D, los puntos se ajustan a una sola curva , mientras que en la interpolación Spline
#' los puntos se ajustan a una función por partes definida con polinomios llamados splines.

#'La función UnivariateSpline() toma xsy ys produce una función invocable que se puede llamar con new xs.

# from scipy.interpolate import UnivariateSpline
# import numpy as np

# xs = np.arange(10)
# ys = xs**2 + np.sin(xs) + 1

# interp_func = UnivariateSpline(xs, ys)

# newarr = interp_func(np.arange(2.1, 3, 0.1))

# print(newarr)

#'INTERPOLACION CON FUNCION DE BASE RADIAL

#'La función de base radial es una función que se define correspondiente a un punto de referencia fijo.
#'La funcion Rbf() también toma xsy ys como argumentos y produce una función invocable que se puede llamar
#' con new xs.

#c Interpola los siguientes xs e ys usando rbf y encuentra valores para 2.1, 2.2... 2.9:

from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)