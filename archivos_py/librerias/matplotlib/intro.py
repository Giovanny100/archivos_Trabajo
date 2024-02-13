
#* Create a graph

import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(-10,11)
# y = pow(x,2)
# plt.plot(x,y,'o',  color = 'green')
# plt.title('F(X) = X^2')

#*Si no se especifican os puntos de x se toman automaticamente como: range(0,len(y)):

y = np.arange(-4,4,1)

#* Parametros de estilo:

#? marker: cambia la representacion de cada punto
#? ms: cambia el tamaño de los puntos
#? mec: cambia color de contorno de la figura de los puntos
#? mfc: cambiar el color de relleno de los puntos
#? ls: cambia el estilo de la linea de grafico
#? c: cambiar el color del grafico
#? linewidth: lw: cambiar el grosor de la linea

plt.plot(y, marker = '*', c = 'yellow', ms = 20, mec = 'hotpink', mfc = '#4CAF50', linewidth = 15)

plt.show()