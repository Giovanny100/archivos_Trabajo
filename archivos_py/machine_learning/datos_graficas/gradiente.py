import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import GroupKFold

# Función aún más compleja
def super_complex_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2)) * np.cos(x) + np.cos(np.sqrt(x**2 + y**2)) * np.sin(y) + np.sin(x*y) + np.cos(x+y)

# Generar datos para el gráfico
x = np.linspace(-2, 2, 100)
y = np.linspace(-1, 3, 100)
xx, yy = np.meshgrid(x, y)
z = super_complex_function(xx, yy)

# Punto mínimo
min_point = np.array([1, 1])
min_value = super_complex_function(*min_point)

# Punto de silla
saddle_point = np.array([1, 1])
saddle_value = super_complex_function(*saddle_point)

# Crear una figura 3D con fondo oscuro
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')  # Fondo oscuro

# Graficar la función aún más compleja con colores más brillantes (nipy_spectral)
curve = ax.plot_surface(xx, yy, z, cmap='nipy_spectral', alpha=0.8, antialiased=True)

# Agregar el mapa de calor (contornos)
contour = ax.contourf(xx, yy, z, zdir='z', offset=np.min(z), cmap='viridis', alpha=0.6)

# Mostrar el punto mínimo y el punto de silla en el gráfico
ax.scatter(*min_point, min_value, color='gold', s=100, label='Punto Mínimo')
ax.scatter(*saddle_point, saddle_value, color='red', s=100, label='Punto de Silla')

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Función Aún Más Compleja con Puntos Mínimo y de Silla, y Colores Brillantes')

# Configurar la leyenda
ax.legend()

# Mostrar el gráfico
plt.show()