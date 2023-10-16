
#'                     VISUALIZAR DISTRIBUCIONES ALATORIAS (MODULO SEABORN)

#' Seaborn es una libreria que utiliza matplotlib en su fuente para graficar distribuciones de datos aleatorios

#? DISPLOTS: Significa grafico de distribucion, toma como entrada una matriz y grafica su distribucion de datos
#! Se requiere importar el objeto pyplot de matplotlib para graficar

import matplotlib.pyplot as plt

import seaborn as sns

# sns.distplot([0,1,2,3,4,5]) #* Devuelve una grafica de distribucion normal

# plt.show()

#c Graficar una distribucion sin el histograma:

sns.distplot([0, 1, 2, 3, 4, 5], hist=False) #*Devuelve una grafica de distribucion sin el histograma

# plt.show()


