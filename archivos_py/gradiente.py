import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

# Definir una combinación de funciones trigonométricas
def f(x):
    return np.sin(x) + 0.5*np.sin(2*x) + 0.2*np.sin(3*x) + 0.1*np.sin(5*x)

# Calcular la derivada de la función
def df(x):
    return np.cos(x) + np.cos(2*x) + 0.6*np.cos(3*x) + 0.5*np.cos(5*x)

# Generar datos para el gráfico
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = f(x)

# Encontrar máximos y mínimos locales
local_maxima_indices = argrelextrema(y, np.greater)[0]
local_minima_indices = argrelextrema(y, np.less)[0]

# Configurar el estilo oscuro
plt.style.use('dark_background')

# Graficar la función
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Combinación de Funciones Seno', color='cyan', linewidth=3)

# Resaltar puntos de máximos y mínimos por encima del gráfico
plt.scatter(x[local_maxima_indices], y[local_maxima_indices], color='red', marker='o', label='Máximos Locales', zorder=5)
plt.scatter(x[local_minima_indices], y[local_minima_indices], color='blue', marker='o', label='Mínimos Locales', zorder=5)

# Agregar líneas tangentes para mostrar la pendiente en cada punto
for i in local_maxima_indices:
    tangent_line = lambda xx: f(x[i]) + df(x[i]) * (xx - x[i])
    plt.plot(x[i:i+50], tangent_line(x[i:i+50]), color='red', linestyle='--')

for i in local_minima_indices:
    tangent_line = lambda xx: f(x[i]) + df(x[i]) * (xx - x[i])
    plt.plot(x[i:i+50], tangent_line(x[i:i+50]), color='blue', linestyle='--')

# Configurar la leyenda y mostrar el gráfico
plt.legend()
plt.title('Combinación de Funciones Seno con Múltiples Curvas y Tangentes en Máximos y Mínimos Locales')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
