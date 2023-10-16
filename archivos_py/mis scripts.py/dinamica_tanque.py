import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define la ecuación diferencial
def f(t, h):
    return 0.126530612244898 - (0.0612244897959184*np.sqrt(h))

# Define el intervalo de tiempo
t_span = [0, 500]

# Define la condición inicial
y0 = [1]

# Resuelve la ecuación diferencial
sol = solve_ivp(f, t_span, y0)

# Gráfica la solución
plt.plot(sol.t, sol.y[0], '-o')
plt.xlabel('tiempo')
plt.ylabel('y(t)')
plt.show()
