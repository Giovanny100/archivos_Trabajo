
import numpy as np
#* Matriz de datos:
data = np.array([
    [4,4,5],
    [5,5,3],
    [5,4,3],
    [4,3,3],
    [6,4,3],
    [6,5,3],
    [4,3,4],
    [5,3,5]
])

#' SUMA DE CUADRADOS TOTALES
#* Suma de datos totales:
s_t = 0
for xi in np.nditer(data):
    s_t = s_t + xi
# print(s_t)

#* Tamaño total de muestra y grados de libertad:

N = len(data) * len(data[0])

gl = N - 1

#* Media total de los datos (Gran Media):

med_tot = np.mean(data)

#* Calculo de SC(totales):
sct = 0
for xi in np.nditer(data):
    c = pow((xi - med_tot),2)
    sct = sct + c
print(f'La suma de cuadrados totales es: {sct}')
#' SUMA DE CUADRADOS ENTRE GRUPOS

#* Tamaño de muestras por tratamiento:

n = len(data)

#* Numero de tratamientos y grados de libertad:

num_trat = len(data[0])
gle = num_trat - 1

print(f'Los grados de libertad  entre grupos son: {gle}')

#? Suma de elementos por tratamientos:
sum = 0
for i in data:
    sum = sum + i
tot_T = sum
# print(tot_T)

#? Suma de los totales por tratamiento:
s_t_t = 0
for j in tot_T:
    s_t_t = j + s_t_t

#? Media de tratamientos:
med_trat = np.array([])
for s in tot_T:
    m = np.array(s/n)
    med_trat = np.append(med_trat, m)
# print(med_trat)

#* Calculo de SC(entre):

v = 0

for j in tot_T:
    v = (j**2)/n + v
sce = v - (pow(s_t,2)/N)

print(f'Las suma de cuadrados entre grupos es: {sce}')

SCe =sce/gle

print(f'Los cuadrados medios entre grupos es (Varianza): {SCe}')

#' SUMA DE CUADRADOS DENTRO DE GRUPOS

scd = sct - sce
gld = N - num_trat

print(f'Los grados de libertad dentro de grupos es: {gld}')

print(f'Las suma de cuadrados dentro de los grupos es: {scd}')

SCd = scd/gld

print(f'Los cuadrados medios dentro de los grupos es (Varianza): {SCd}')

RV = SCe/SCd
print(f'La razon de varianzas (RV) = {RV}')