#PARA UNA ESFER A PODEMOS ESTABLECER:
from scipy.integrate import simps
import matplotlib.pyplot as plt
import numpy as np

R = 1
x = np.linspace(-R, R)
y = np.pi*(1-x**2)

volumen = simps(y,x)
vol_exacto = 4/3*np.pi*R**3
print(volumen)
print(vol_exacto)

x = np.array([0,0.2,0.4,0.6,0.65])
r_A = -np.array([39,53,59,38,25])

FA0 = 50  #Kmol/Litro

y = FA0/-r_A

volumen = simps(y,x)

print(f'El volumen necesario para una conversion del 65% es de: {volumen : 1.2f} m3')

plt.plot(x,y, color = 'black')
plt.title('VARIACION DE LA CONCENTRACION POR EFECTO DE DIFUSION d[CA]/dt')
plt.xlabel('Conversión')
plt.ylabel('Integrando')

plt.show()

vols = []

for i in range(0, len(x)):
    vol = simps(y[0:i+1], x[0:i+1])
    vols.append(vol)
    print(f'El volumen es: {vol} a la conversion de {x[i]}')

#Para los fenomenos de superficie en el electrodo:

'''
Se puede suponer v = 0 , dv/dt = k1
Cada arreglo: n = 8
Diametro nominal= 24 cm
El termino de la ec. de navier stokes: M = 0.0247
No se tiene regimen de flujo constante ni las exs.
Corregir la no convergencia de la ecuacion por medio del ajuste de parametros

'''