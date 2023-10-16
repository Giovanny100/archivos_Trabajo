import numpy as np
import matplotlib.pyplot as plt


# Creamos una matriz 2D con valores 0 (blanco)
matriz = np.zeros((10, 10))

# Definimos las posiciones de los pixeles que representan el cuadrado
matriz[2:8, 2:8] = 1

# Creamos el gráfico utilizando Matplotlib
plt.imshow(matriz, cmap='gray', interpolation='none')
plt.show()



