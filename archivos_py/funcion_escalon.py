import numpy as np
import matplotlib.pyplot as plt

# Definir la función para una línea recta
def linea_recta(x):
    # Ajustar la pendiente (m) y la intersección (b) según tus preferencias
    m = 2
    b = 1
    return m * x + b

# Generar datos x de -5 a 5 con paso de 0.1
x = np.arange(-5, 5, 0.1)

# Calcular los valores de la línea recta para cada x
y = linea_recta(x)

# Estilo y colores más elegantes
plt.style.use('seaborn-dark-palette')
color = 'violet'

# Graficar la línea recta con la intersección en el eje de las ordenadas
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Línea Recta', color=color, linewidth=3)
plt.scatter(0, linea_recta(0), color='red', label='Intersección en Y', s=100)  # Punto de intersección
plt.title('Línea Recta', fontsize=18, fontweight='bold', color='darkblue')
plt.xlabel('X', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Y', fontsize=14, fontweight='bold', color='darkblue')
plt.axhline(0, color='black', linewidth=2, label='Eje Y')  # Eje Y en negro y etiqueta
plt.axvline(0, color='black', linewidth=2, label='Eje X')  # Eje X en negro y etiqueta
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(loc='upper left', fontsize=12, frameon=True, facecolor='white', edgecolor='black')
plt.xticks(fontsize=12, color='darkblue')
plt.yticks(fontsize=12, color='darkblue')
plt.tight_layout()
plt.show()
