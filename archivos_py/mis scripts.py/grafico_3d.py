import matplotlib.pyplot as plt
import numpy as np

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definir datos de ejemplo
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  #* Reemplazar esta función con la que desees graficar en 3D

# Graficar la superficie en 3D
ax.plot_surface(X, Y, Z, cmap='viridis')

# Etiquetas de los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Título del gráfico
ax.set_title('Gráfico 3D con Etiquetas de Ejes')

# Mostrar el gráfico
plt.show()
