import matplotlib.pyplot as plt
import numpy as np

# Datos de niveles de hormonas tiroideas con valores aleatorios fuera de los rangos normales
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

# Generar valores aleatorios para TSH (fuera de los rangos normales)
tsh = np.random.uniform(0.05, 0.9, 12)  # Niveles de TSH (mUI/L)
# Generar valores aleatorios para T4 (fuera de los rangos normales)
t4 = np.random.uniform(10.0, 12.8, 12)  # Niveles de T4 (µg/dL)
# Generar valores aleatorios para T3 (fuera de los rangos normales)
t3 = np.random.uniform(160, 250, 12)     # Niveles de T3 (ng/dL)

# Límites superiores e inferiores para cada hormona
limite_superior_tsh = 2.5  # Límite superior de TSH (mUI/L)
limite_inferior_tsh = 0.4  # Límite inferior de TSH (mUI/L)
limite_superior_t4 = 12.0  # Límite superior de T4 (µg/dL)
limite_inferior_t4 = 4.5   # Límite inferior de T4 (µg/dL)
limite_superior_t3 = 200   # Límite superior de T3 (ng/dL)
limite_inferior_t3 = 80    # Límite inferior de T3 (ng/dL)

# Crear la figura con fondo morado tenue
fig = plt.figure(figsize=(12, 4))
fig.patch.set_facecolor('#F0E6F7')  # Cambio de fondo de la ventana principal

# Gráfico para TSH
ax1 = plt.subplot(1, 3, 1)
ax1.set_facecolor('#F0E6F7')  # Cambio de fondo del gráfico TSH
ax1.plot(meses, tsh, marker='o', color='tomato', linewidth=2, label='TSH')
ax1.axhline(y=limite_superior_tsh, color='red', linestyle='--', label='Límite Superior')
ax1.axhline(y=limite_inferior_tsh, color='c', linestyle='--', label='Límite Inferior')
ax1.set_title('Niveles de TSH', fontsize=14)
ax1.set_xlabel('Mes', fontsize=12)
ax1.set_ylabel('Niveles (mUI/L)', fontsize=12)
ax1.legend(fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)

# Gráfico para T4
ax2 = plt.subplot(1, 3, 2)
ax2.set_facecolor('#F0E6F7')  # Cambio de fondo del gráfico T4
ax2.plot(meses, t4, marker='o', color='mediumseagreen', linewidth=2, label='T4')
ax2.axhline(y=limite_superior_t4, color='red', linestyle='--', label='Límite Superior')
ax2.axhline(y=limite_inferior_t4, color='c', linestyle='--', label='Límite Inferior')
ax2.set_title('Niveles de T4', fontsize=14)
ax2.set_xlabel('Mes', fontsize=12)
ax2.set_ylabel('Niveles (µg/dL)', fontsize=12)
ax2.legend(fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.7)

# Gráfico para T3
ax3 = plt.subplot(1, 3, 3)
ax3.set_facecolor('#F0E6F7')  # Cambio de fondo del gráfico T3
ax3.plot(meses, t3, marker='o', color='cornflowerblue', linewidth=2, label='T3')
ax3.axhline(y=limite_superior_t3, color='red', linestyle='--', label='Límite Superior')
ax3.axhline(y=limite_inferior_t3, color='c', linestyle='--', label='Límite Inferior')
ax3.set_title('Niveles de T3', fontsize=14)
ax3.set_xlabel('Mes', fontsize=12)
ax3.set_ylabel('Niveles (ng/dL)', fontsize=12)
ax3.legend(fontsize=10)
ax3.grid(True, linestyle='--', alpha=0.7)

# Ajustar el espacio entre subgráficos
plt.tight_layout()

# Mostrar los gráficos
plt.show()
