
#' Sepueden establecer marcas para cada punto graficado:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([range(10)])
y = np.array([range(10)])

plt.plot(x,y, marker = 'D') #* El argumento marker dara una forma a cada punto en este caso D es diamantes
plt.show()

