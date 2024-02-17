import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, norm
import numpy as np

#' Generar datos aleatorios con una distribución normal:

datos = np.load('C:/Users/mar_amez/Desktop/gio/archivos_py/matrices/matriz743.npy')

#' Crear histograma:

plt.figure(figsize=(10, 5))
plt.hist(datos, bins=30, color='blue', alpha=0.7, density=True) # Modificar los parámetros según tus necesidades
plt.title('Histograma de datos')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()


# #' Realizar prueba de normalidad de Shapiro-Wilk

# stat, p_valor = shapiro(datos)
# print("Estadístico de Shapiro-Wilk:", stat)
# print("Valor p:", p_valor)
# if p_valor > 0.05:
#     print("No se rechaza la hipótesis nula (los datos provienen de una distribución normal)")
# else:
#     print("Se rechaza la hipótesis nula (los datos no provienen de una distribución normal)")
