# import matplotlib.pyplot as plt
# import numpy as np

# #' Supongamos que tienes un array de edades y géneros:
# media = 75.5
# desviacion_estandar = 10
# edades = np.random.normal(media, desviacion_estandar, 1000)
# genero = np.random.normal(media, desviacion_estandar, 1000)

# # Filtra las edades por género:

# edades_hombres = edades[genero == 0]
# edades_mujeres = edades[genero == 1]

# # Crea un gráfico de dispersión
# plt.scatter(edades_hombres, genero[genero == 0], label='Hombres', color='blue')
# plt.scatter(edades_mujeres, genero[genero == 1], label='Mujeres', color='pink')

# # Añade etiquetas y título
# plt.xlabel('Edad')
# plt.ylabel('Género (0 = Hombres, 1 = Mujeres)')
# plt.title('Gráfico de Dispersión de Edad por Género')

# # Añade una leyenda
# plt.legend()

# # Muestra el gráfico
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Supongamos que tienes un array de edades y géneros:
media = 75.5
desviacion_estandar = 10

# Genera dos arrays de edades con distribuciones normales diferentes para hombres y mujeres
edades_hombres = np.random.normal(media, desviacion_estandar, 1000)
edades_mujeres = np.random.normal(media, desviacion_estandar, 1000)

# Genera arrays de género (0 para hombres, 1 para mujeres)
genero_hombres = np.zeros(1000)
genero_mujeres = np.ones(1000) data gfvb

# Combina los arrays de edades y género
edades = np.concatenate([edades_hombres, edades_mujeres])
genero = np.concatenate([genero_hombres, genero_mujeres])

# Crea un gráfico de dispersión
plt.scatter(edades, genero, c=genero, cmap='viridis', label=['Hombres', 'Mujeres'])

# Añade etiquetas y título
plt.xlabel('Edad')
plt.ylabel('Género (0 = Hombres, 1 = Mujeres)')
plt.title('Gráfico de Dispersión de Edad por Género')

# Añade una leyenda
plt.legend()

# Muestra el gráfico
plt.show()


