'''
EL CODIGO DADO INCLUYE UNA LISTA DE ALTURAS PARA VARIOS JUGADORES DE BALONCESTO.

HAY QUE CALCULAR Y GENERAR CUANTOS JUGADORES ESTAN EN EL RANGO DE DESVIACION ESTANDAR DE LA MEDIA.
'''


import numpy as np

players = np.array([180,172,178,185,190,195,192,200,210,190])
media2 = np.sum(players)/players.size
var = np.sum((players - media2)**2)/players.size

desv_est = pow(var,0.5)

limi_inferior = media2 - desv_est
limi_sup = media2 + desv_est
n = 0
for p in players:
    if limi_inferior < p and limi_sup > p:
        n += 1
print(n)