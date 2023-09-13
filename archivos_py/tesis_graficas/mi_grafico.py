import numpy as np
import matplotlib.pyplot as plt

funcion = lambda x : -1 * (pow(1 -3*x - pow(x, 2), 0.5) + 1)

x = np.linspace(-5,5,1000000)

f = funcion(x)

plt.figure(figsize = (8,8))
plt.plot(x,f,label="Fucnion libro", color = 'red')
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.legend()
plt.grid(True)

plt.axhline(0, color='black', linewidth= 1.1)
plt.axvline(0, color='black', linewidth= 1.1)

plt.show()