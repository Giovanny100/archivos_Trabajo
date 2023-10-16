

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Datos de ejemplo (reemplaza estos datos con tus propios datos)
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2.7, 7.4, 20.1, 54.6, 148.4])

# Definición de la función exponencial
def funcion_exponencial(X, a, b):
    return a * np.exp(b * X)

# Ajuste de la curva exponencial a los datos
parametros_optimizados, covarianza = curve_fit(funcion_exponencial, X, Y)

# Extracción de los parámetros a y b
a_optimizado, b_optimizado = parametros_optimizados

# Creación de una función ajustada basada en los parámetros optimizados
Y_predicho = funcion_exponencial(X, a_optimizado, b_optimizado)

# Visualización de los datos y la curva ajustada
plt.scatter(X, Y, label='Datos reales')
plt.plot(X, Y_predicho, color='red', label='Curva ajustada')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Impresión de los parámetros optimizados
print(f"Coeficiente de escala (a): {a_optimizado}")
print(f"Coeficiente de tasa (b): {b_optimizado}")
