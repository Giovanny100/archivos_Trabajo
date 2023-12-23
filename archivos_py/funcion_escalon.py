import numpy as np
import matplotlib.pyplot as plt

# Definir la función ReLU
def relu(x):
    return np.maximum(0, x)

# Generar datos x de -7 a 7 con paso de 0.1
x = np.arange(-7, 7, 0.1)

# Calcular los valores de la función ReLU para cada x
y = relu(x)

# Estilo y colores más elegantes
plt.style.use('seaborn-dark-palette')
color = 'springgreen'

# Graficar la función ReLU
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='ReLU', color=color, linewidth=14)
plt.title('ReLU', fontsize=16, fontweight='bold', color='orange')
plt.xlabel('X', fontsize=12, fontweight='bold', color='navy')
plt.ylabel('Y', fontsize=12, fontweight='bold', color='navy')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(loc='upper left', fontsize=12, frameon=True, facecolor='white', edgecolor='black')
plt.xticks(fontsize=10, color='navy')
plt.yticks(fontsize=10, color='navy')
plt.tight_layout()
plt.show()
