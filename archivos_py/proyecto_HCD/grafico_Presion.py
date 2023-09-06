import matplotlib.pyplot as plt
import datetime

# Datos de ejemplo: fecha y presión arterial sistólica y diastólica
fechas = [datetime.datetime(2023, i, 1) for i in range(1, 13)]  # Fechas de enero a diciembre
presion_sistolica = [120, 122, 118, 124, 118, 126, 122, 120, 124, 118, 126, 122]  # Valores mensuales
presion_diastolica = [80, 82, 78, 80, 76, 82, 80, 78, 82, 76, 84, 80]  # Valores mensuales

# Crear el gráfico con fondo gris más fuerte
plt.style.use('seaborn-white')
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#E6E6FA')  # Fondo gris más fuerte

# Colores de las líneas en tonos pastel
color_sistolica = 'pink'  # Rosa pastel
color_diastolica = 'lightskyblue'  # Color pastel 2
estilo_linea = '-'

# Gráficos de presión sistólica y diastólica
ax.plot(fechas, presion_sistolica, marker='o', label='Presión Sistólica', color=color_sistolica, linestyle=estilo_linea, linewidth=2)
ax.plot(fechas, presion_diastolica, marker='o', label='Presión Diastólica', color=color_diastolica, linestyle=estilo_linea, linewidth=2)

# Agregar sombreado a las líneas con un color más tenue
ax.fill_between(fechas, [ps - 2 for ps in presion_sistolica], [ps + 2 for ps in presion_sistolica], color=color_sistolica, alpha=0.3)
ax.fill_between(fechas, [pd - 2 for pd in presion_diastolica], [pd + 2 for pd in presion_diastolica], color=color_diastolica, alpha=0.3)

# Personalización del gráfico
nombre_paciente = "\"Nombre del paciente\""
ax.set_title(f"Presión Arterial de {nombre_paciente}", fontsize=16)
ax.set_xlabel('Fecha', fontsize=12)
ax.set_ylabel('Presión Arterial (mm Hg)', fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)

# Formato de las fechas en el eje x
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator(interval=1))

# Mostrar los valores de presión arterial en el eje y
ax.yaxis.set_ticks(range(60, 171, 10))

# Resaltar las líneas con texto sombreado
for i in range(len(fechas)):
    ax.annotate(f"{presion_sistolica[i]}", (fechas[i], presion_sistolica[i]), textcoords="offset points", xytext=(0,10), ha='center')
    ax.annotate(f"{presion_diastolica[i]}", (fechas[i], presion_diastolica[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Mostrar el gráfico con margen y estilo
plt.tight_layout()
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.legend()
fig.set_facecolor('#E6E6FA')
plt.show()

