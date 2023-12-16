import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# Datos de ejemplo
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = 2 * x + 3 * y  # Ecuación del plano

# Puntos de dispersión aleatorios para agregar
num_puntos = 200
x_dispersion = np.random.uniform(-7, 7, num_puntos)
y_dispersion = np.random.uniform(-7, 7, num_puntos)
z_dispersion = 2 * x_dispersion + 3 * y_dispersion + np.random.normal(0, 10, num_puntos)  # Agregar algo de variabilidad

# Crear la figura y los ejes tridimensionales
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Configurar fondo oscuro
ax.set_facecolor('#121212')  # Color de fondo oscuro

# Crear un gradiente de color en el plano
cmap = LinearSegmentedColormap.from_list('gradiente', ['#FFFFFF', '#9575cb'], N=len(z))
surf = ax.plot_surface(x, y, z, cmap=cmap, rstride=100, cstride=100, linewidth=0.5, antialiased=True, shade=True)

# Añadir contornos
cset = ax.contour(x, y, z, zdir='z', offset=np.min(z), cmap='viridis', linestyles='dashed', linewidths=1)

# Agregar puntos de dispersión
ax.scatter(x_dispersion, y_dispersion, z_dispersion, c='white', marker='o', s=30, label='Puntos de Dispersión')

# Barra de color
cbar = fig.colorbar(surf, ax=ax, pad=0.1, aspect=10)
cbar.set_label('Esperanza de vida')

# Etiquetas de los ejes y título
ax.set_xlabel('X1:Revisión Médica', fontsize=12, color='white')  # Etiquetas en color blanco
ax.set_ylabel('X2:Riesgo de Trabajo', fontsize=12, color='white')
ax.set_zlabel('X3:Ejercicio', fontsize=12, color='white')
ax.set_title('Plano Tridimensional con Puntos de Dispersión', fontsize=14, color='white')

# Ajustes de estilo
ax.grid(True)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.w_xaxis.line.set_lw(0)
ax.w_yaxis.line.set_lw(0)
ax.w_zaxis.line.set_lw(0)

# Añadir grillado al plano
ax.set_box_aspect([1, 1, 1])
ax.grid(True, linestyle='--', alpha=0.6, linewidth=0.5)

# Rotar el gráfico para una mejor visualización
ax.view_init(elev=20, azim=-45)

# Mostrar el gráfico
plt.show()