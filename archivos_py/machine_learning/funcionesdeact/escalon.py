import numpy as np
import matplotlib.pyplot as plt

x = list(range(-100,100))
y = []
def f(x):
    for i in x:
        if i <= 0:
            y.append(0)
        else:
            y.append(1)
    return y
y = f(x)
plt.plot(x, y)
plt.show()