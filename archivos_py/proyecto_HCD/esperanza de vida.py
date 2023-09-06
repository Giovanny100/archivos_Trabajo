import matplotlib.pyplot as plt
import random

# Datos de ejemplo
años = list(range(2024, 2037))  # Años de 2020 a 2050
esperanza_de_vida_mujeres = [80 + random.uniform(-2, 2) for _ in años]  # Esperanza de vida para mujeres con fluctuaciones aleatorias

# Crear la gráfica con estilo y detalle
plt.figure(figsize=(12, 8))
plt.style.use('seaborn-whitegrid')

fig, ax = plt.subplots()
ax.plot(años, esperanza_de_vida_mujeres, color='deeppink', marker='o', linestyle='-', linewidth=2, markersize=8, label='Esperanza de Vida (Genero Femenino)')
ax.fill_between(años, [e - 1.5 for e in esperanza_de_vida_mujeres], [e + 1.5 for e in esperanza_de_vida_mujeres], color='mistyrose', alpha=0.5)

ax.set_title('Esperanza de Vida para la paciente "Nombre"', fontsize=18, fontweight='bold')
ax.set_xlabel('Año', fontsize=14)
ax.set_ylabel('Longevidad', fontsize=14)
ax.legend(fontsize=12)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_xticks(años[::2])
ax.set_ylim(min(esperanza_de_vida_mujeres) - 3, max(esperanza_de_vida_mujeres) + 3)
ax.set_facecolor('#E6E6FA')  # Fondo gris claro

plt.xticks(rotation=45)
plt.yticks(fontsize=12)
plt.tight_layout()

# Añadir anotación con estilo
ax.annotate('Variaciones debido a situación clínica', xy=(2035, max(esperanza_de_vida_mujeres) - 1), xytext=(2030, max(esperanza_de_vida_mujeres) + 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05, connectionstyle="arc3,rad=.2"), fontsize=12, color='black')

# Efecto sombra
ax.plot(años, esperanza_de_vida_mujeres, color='gray', alpha=0.3, linewidth=5)
fig.set_facecolor('#E6E6FA')
plt.show()
