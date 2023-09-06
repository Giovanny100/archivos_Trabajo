import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math as m
import seaborn as sn

# Crear un array de valores x
x = np.linspace(-2*np.pi, 2*np.pi, 50)

# Crear las funciones y1 y y2
y1 = np.sin(2*x)+1
y2 = np.sin(x)

# Crear una figura y un eje
fig, ax = plt.subplots()

# Graficar las funciones en el mismo gráfico

ax.plot(x, y1, label='sin(5x)')
ax.plot(x, y2, label='sin(x)')

# Agregar título y etiquetas de los ejes
ax.set_title('Funciones trigonométricas')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Agregar una leyenda
ax.legend()

# Mostrar el gráfico
plt.show()

