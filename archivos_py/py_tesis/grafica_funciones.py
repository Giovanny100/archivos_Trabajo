import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(6*x)

x = np.linspace(-50, 50,100000*5)

plt.plot(x, f(x))

plt.show()