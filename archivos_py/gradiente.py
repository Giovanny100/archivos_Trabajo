import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definimos una función más compleja y colorida
def funcion_ejemplo(x, y):
    return np.sin(np.sqrt(x**2 + y**2)) * np.cos(x) * np.cos(y)

# Derivadas parciales de la función respecto a x e y
def derivada_parcial_x(x, y):
    r = np.sqrt(x**2 + y**2)
    return np.cos(r) * np.cos(x) * np.cos(y) - (x * np.sin(r) * np.cos(x) * np.cos(y)) / r

def derivada_parcial_y(x, y):
    r = np.sqrt(x**2 + y**2)
    return np.cos(r) * np.cos(x) * np.cos(y) - (y * np.sin(r) * np.cos(x) * np.cos(y)) / r

# Descenso del gradiente
def descenso_gradiente(learning_rate, num_iteraciones):
    # Punto de inicio
    punto_inicial = np.array([4.0, 4.0])

    # Listas para almacenar los valores de x, y y la función en cada iteración
    x_vals = []
    y_vals = []
    z_vals = []

    for _ in range(num_iteraciones):
        x_vals.append(punto_inicial[0])
        y_vals.append(punto_inicial[1])
        z_vals.append(funcion_ejemplo(punto_inicial[0], punto_inicial[1]))

        # Actualizamos el punto usando el descenso del gradiente
        punto_inicial[0] -= learning_rate * derivada_parcial_x(punto_inicial[0], punto_inicial[1])
        punto_inicial[1] -= learning_rate * derivada_parcial_y(punto_inicial[0], punto_inicial[1])

    return x_vals, y_vals, z_vals

# Parámetros del descenso del gradiente
learning_rate = 0.1
num_iteraciones = 50

# Obtener valores para graficar
x_vals, y_vals, z_vals = descenso_gradiente(learning_rate, num_iteraciones)

# Crear una figura 3D con fondo oscuro
fig = plt.figure(figsize=(8, 6), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Graficar la función de ejemplo con colores morados
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = funcion_ejemplo(x, y)
surf = ax.plot_surface(x, y, z, alpha=0.7, cmap='Purples')  # Cambio de color a tonos morados

# Resaltar el grillado con líneas blancas
ax.w_xaxis.set_pane_color((0, 0, 0, 1))
ax.w_yaxis.set_pane_color((0, 0, 0, 1))
ax.w_zaxis.set_pane_color((0, 0, 0, 1))

# Graficar el descenso del gradiente con un color violeta vibrante y vectores
ax.quiver(x_vals[:-1], y_vals[:-1], z_vals[:-1], np.diff(x_vals), np.diff(y_vals), np.diff(z_vals), color='violet', length=0.1, normalize=True, label='Descenso del Gradiente')

# Configuraciones adicionales
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Función')
ax.legend()

# Configurar colores de fondo y cuadrícula
ax.xaxis.pane.fill = True
ax.yaxis.pane.fill = True
ax.zaxis.pane.fill = True
ax.grid(True)

# Mostrar la gráfica
plt.show()
