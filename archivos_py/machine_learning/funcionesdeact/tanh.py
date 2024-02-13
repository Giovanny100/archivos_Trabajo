import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100,100,50)
y = []

def f(x):
    for i in x:
        y.append((np.exp(i) - np.exp(-i))/(np.exp(i) + np.exp(-i)))
    return y

y = f(x)

plt.plot(x,y)
plt.show()