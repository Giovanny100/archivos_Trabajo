
#' En machine learning se suele trabajar con conjutntos de datos grandes. Podemos aprovechar Numpy para esto

#c El metodo np.random.uniform(x,y,z) : Para generar Z numeros aleatorios entre el rango(x,y) abirto en Y

#* Creemos un dataset aleatorio y visualicemos su distribucion en un histograma:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 1000) #* Mil datos de entre 0 y 4

# plt.hist(x, 100)
# plt.show()

#* Para obtener datos distribuidos normalemtne:

y = numpy.random.normal(5.0, 1.0, 4000)

plt.hist(y, 100)
plt.title('Distribucion de datos Diabetes')
plt.show()