x = list(range(5))

print(x[1:-1])

import sympy as sp

x = sp.Symbol('x')

y = x**2 + 1

print(y.integrate((x,1,3)))