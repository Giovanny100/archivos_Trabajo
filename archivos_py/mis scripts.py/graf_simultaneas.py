import matplotlib.pyplot as plt
import numpy as np

fun_1 = lambda x: np.log(x)
fun_2 = lambda x: np.sqrt(x)
# fun_3 = lambda x: 4*(0.68*abs(x) - 2)

x = np.linspace(-10,10,1000000)

y_min = 0
y_max= 5

f = fun_1(x)
g = fun_2(x)
# h = fun_3(x)

plt.figure(figsize = (5,5))
plt.plot(x, f,label = 'Logaritmo natural', color = 'red')
plt.plot(x,g,label = 'Raiz cuadrada',color = 'blue')
# plt.plot(x,h,label = 'raiz sexta',color = 'red')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.axhline(0,color='black', linewidth = 1.2)
plt.axvline(0,color='black', linewidth = 1.2)
# plt.axhline(1,color='red', linewidth = 1.2)
plt.ylim(y_min, y_max)
plt.show()


