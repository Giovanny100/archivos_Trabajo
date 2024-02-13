import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, norm
import numpy as np

#' Generar datos aleatorios con una distribución normal:

datos = np.random.normal(loc=0, scale=1, size=1000)

#' Crear histograma:

plt.figure(figsize=(10, 5))
sns.histplot(datos, kde=True, color='skyblue', bins=30)
plt.title('Histograma de datos')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()

# #' Crear gráfico de probabilidad normal (QQ plot):

# plt.figure(figsize=(8, 8))
# norm_values = np.random.normal(loc=np.mean(datos), scale=np.std(datos), size=len(datos))
# sns.scatterplot(np.sort(norm_values), np.sort(datos), color='blue', label='Datos')
# sns.lineplot(norm.ppf([0.01, 0.99]), norm.ppf([0.01, 0.99]), color='red', label='Recta de referencia')
# plt.title('Gráfico de Probabilidad Normal (QQ plot)')
# plt.xlabel('Cuantiles teóricos')
# plt.ylabel('Cuantiles observados')
# plt.legend()
# plt.show()

# #' Realizar prueba de normalidad de Shapiro-Wilk

# stat, p_valor = shapiro(datos)
# print("Estadístico de Shapiro-Wilk:", stat)
# print("Valor p:", p_valor)
# if p_valor > 0.05:
#     print("No se rechaza la hipótesis nula (los datos provienen de una distribución normal)")
# else:
#     print("Se rechaza la hipótesis nula (los datos no provienen de una distribución normal)")
