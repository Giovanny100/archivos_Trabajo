import math

values = [5, 5.2172]

def f(x):
    return math.sqrt(x**2 - 4*x - (12*math.sqrt(6*x))+ 61)

for i in values:
    print(f(i))


