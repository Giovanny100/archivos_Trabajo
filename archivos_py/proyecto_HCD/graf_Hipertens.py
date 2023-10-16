import matplotlib.pyplot as plt
import datetime

# Datos de ejemplo: fecha y presión arterial sistólica y diastólica
fechas = [datetime.datetime(2023, i, 1) for i in range(1, 13)]  # Fechas de enero a diciembre
presion_sistolica = [140, 145, 148, 152, 150, 155, 160, 158, 150, 155, 160, 155]  # Valores mensuales (hipertensión)
presion_diastolica = [90, 92, 95, 94, 92, 96, 98, 100, 98, 100, 102, 98]  # Valores mensuales (hipertensión)

# Crear el gráfico con fondo gris más fuerte
plt.style.use('seaborn-white')
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#E6E6FA')  # Fondo gris más fuerte

# Colores de las líneas en tonos pastel
color_sistolica = 'pink'  # Rosa pastel
color_diastolica = '#C4B9D9'  # Color pastel 2
estilo_linea = '-'

# Gráficos de presión sistólica y diastólica
ax.plot(fechas, presion_sistolica, marker='o', label='Presión Sistólica', color=color_sistolica, linestyle=estilo_linea, linewidth=2)
ax.plot(fechas, presion_diastolica, marker='o', label='Presión Diastólica', color=color_diastolica, linestyle=estilo_linea, linewidth=2)

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

# Sombreado ligero debajo de las líneas
for i in range(len(fechas)-1):
    ax.fill_between([fechas[i], fechas[i+1]], [presion_sistolica[i], presion_sistolica[i+1]], [presion_diastolica[i], presion_diastolica[i+1]], color='mistyrose', alpha=0.3)

# Mostrar el gráfico con margen y estilo
plt.tight_layout()
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.legend()
fig.set_facecolor('#E6E6FA')  # Cambiar el color de fondo a morado claro
plt.show()