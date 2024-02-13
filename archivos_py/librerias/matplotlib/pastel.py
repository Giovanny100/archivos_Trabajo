
#' Crear graficos de pastel con la funcion pie()
#' Por defecto se comienza en el angulo 0 pero se puede cambiar con startangle

import matplotlib.pyplot as plt
import numpy as np

#? explode() : resaltar las porciones (matriz de valores)
#? shadow = True : agregar somra al grafico de pastel
#? colors = []: Agregar colores especificos a cada elemento con una matriz predefinida
#? Para legend(title = 'Encabezado') : Agregar titulo a las leyendas

yu = np.array([4,2,85,6,2,62])
mis_labels = ['decesos en hospitales','Dcesos por accidentes','Vivos','Enfermos','Muerte natural', 'Desconocidas']
my_exp = [0.2,0.5,0.1,0.2,0.4,0.1]   #* Matriz de resaltado de porciones
colores = ['springgreen','purple','hotpink','violet','lightgreen','gray']
plt.pie(yu, labels = mis_labels, startangle=180, explode = my_exp, shadow = True, colors = colores)
plt.legend()   #* Agregar leyendas de cada seccion
plt.show()

