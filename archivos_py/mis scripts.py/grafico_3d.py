import matplotlib.pyplot as plt
import numpy as np

# Crear una figura 3D con fondo oscuro
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')  # Establecer el color de fondo

# Definir datos de ejemplo con una función más compleja
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2)) + np.cos(X + Y)

# Graficar la superficie en 3D con una combinación de colores
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='white', linewidth=0.5, alpha=0.8)

# Ejecutar un bucle para ajustar el color de fondo de cada barra de color
for c in ax.get_children():
    if isinstance(c, plt.cm.ScalarMappable):
        c.set_cmap('viridis')

# Etiquetas de los ejes
ax.set_xlabel('Eje X', color='white')  # Texto del eje X en blanco
ax.set_ylabel('Eje Y', color='white')  # Texto del eje Y en blanco
ax.set_zlabel('Eje Z', color='white')  # Texto del eje Z en blanco

# Color de los ejes
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='z', colors='white')

# Título del gráfico
ax.set_title('Gráfico 3D Mejorado', color='white')

# Ajustar la elevación y el ángulo de la vista
ax.view_init(elev=20, azim=30)

# Mostrar el gráfico
plt.show()
