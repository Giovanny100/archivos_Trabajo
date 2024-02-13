import math
import numpy as np
import matplotlib.pyplot as plt

x = list(range(-100,100))
y = []

def f(x):
    for i in x:
        y.append(1/(1 + math.exp(-i)))
    return y
y = f(x)

plt.plot(x, y)
plt.show()