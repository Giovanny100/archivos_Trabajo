
#'La funcion bar() sirve para hacer graficos de barras

#' Argumentos de la fucion bar()
#? color = '',Para verticales width = '', Para horizontales height = ''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C','D'])
y = np.random.randint(40, size = 4)

# plt.bar(x,y, width = 0.5)
# plt.show()

#' Grafico horizontal barh(x,y)

plt.barh(x,y, color = 'hotpink', height = 0.4)
plt.show()


