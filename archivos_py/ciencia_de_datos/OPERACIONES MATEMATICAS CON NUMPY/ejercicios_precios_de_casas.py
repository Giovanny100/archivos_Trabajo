'''
THE MATRIX IS GIVEN WITH THE PRICES OF THE HOUSES.

CALCULATE AND GENERATE THE PERCENTAGE OF HOUSES THAT ARE WITHIN ONE STANDARD DEVIATION OF THE MEAN.
'''

import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

media = np.mean(data)
des_est = np.std(data)

lim_inf = media-des_est

lim_sup = media+des_est

datos_in = len(data[(lim_inf < data) & (lim_sup > data) ])

print(datos_in)
porcentaje = (datos_in / len(data))* 100

print(porcentaje)