
#*Se pueden graficar mas de uno en el mismo cuadro usando varios plt.plot

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([1,5,9,8,5,8,15,58])
y2 = np.array([5,8,1,8,8,58,9,15])

# plt.plot(y1)
# plt.plot(y2)
# plt.plot(y1* pow(y2,0.5))
# plt.plot(y1/y2)

#*Tambien se puede en el mismo plt.plot defineinedo las variables por separado

x1 = np.random.rand(8)
x2 = np.random.rand(8)

plt.plot(x1,y1,x2,y2)

plt.title('grafica simultanea')
plt.show()