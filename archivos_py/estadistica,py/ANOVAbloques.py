
#*                                                   MODELO DE BLOQUES COMPLETAMENTE ALEATORIOS


#c NOMBRES DE VARIABLES:

#': Xij = Observaciones individuales
#': Xi = Filas de la matriz (bloques)
#': N = Tamaño de nuestra total
#': n = Numero de Bloques
#': k = Numero de Tratamientos
#': GLtot = Grados de libertad totales
#': GLB = Grados de libertad bloques
#': GLT = Grados de libertad tratamiento
#': GLres = Grados de libertad residuales
#': C = Factor de corrección
#' Tnj = Totales por bloque (filas)
#' Tin = Totales por tratamiento (columnas)
#' Xnj = Medias por bloques
#' Xin = Medias por tratamiento
#' SC = Suma de cuadados totales
#' SCB = Suma de cuadados bloques
#' SCT = Suma de cuadados tratamientos
#' SCres = Suma de cuadados residuales
#' CMT = Error cuadratico medio (tratamientos)
#' CMB = Error cuadratico medio (bloques)
#' CMres = Error cuadratico medio (residuales)
#' RV = Razon de varianzas

import numpy as np

#* MATRIZ DE DATOS:

data = np.array([
    [1.3,2.2,1.8,3.9],
    [1.6,2.4,1.7,4.4],
    [0.5,0.4,0.6,2.0],
    [1.2,2.0,1.5,4.1],
    [1.1,1.8,1.3,3.4],
])

#* TAMAÑOS DE MUESTRAS, TRATAMIENTOS Y BLOQUES

#? N = Tamaño de nuestra total

N = 0
for Xij in np.nditer(data):
    N = N + 1
# print(f'Tamaño total de la muestra: N = {N}')

#? n = Numero de Bloques

n = 0
n = data.shape[0]
# print(f'Numero de bloques: n = {n}')

#? k = Numero de Tratamientos

k = data.shape[1]
# print(f'Numero de tratamientos: k = {k}')

#* GRADOS DE LIBERTAD

#? DF(totales) = kn - 1

GLtot = k*n - 1
# print(f'Los grados de libertad totales son: GLtot = {GLtot}')

#? DF(bloques) = n - 1

GLB = n - 1
# print(f'Los grados de libertad de bloques son: GLB = {GLB}')

#? DF(tratamientos) = k - 1

GLT = k - 1
# print(f'Los grados de libertad de tratamientos son: GLT = {GLT}')

#? DF(residuales) = (kn - 1) - (n - 1) - (k - 1) = (n - 1)(k - 1)

GLres = (n - 1)*(k - 1)
# print(f'Los grados de libertad residuales son: GLres = {GLres}')

#* TOTALES POR BLOQUES

Tnj = []
for xi in data:
    sumas = sum(xi)
    Tnj.append(sumas)
# print(f'Lista de totales por bloques: {Tnj}')

#* MEDIAS POR BLOQUES

Xnj = []
for Ti in Tnj:
    Xnj.append(Ti/k)
# print(f'Lista de medias por bloques: {Xnj}')

#* TOTALES POR TRATAMIENTOS

Tin =  np.sum(data, axis=0)
# print(f'Lista de totales por tratamientos: {Tin}')

#* MEDIAS POR TRATAMIENTOS

Xin = []
for Tj in Tin:
    Xin.append(Tj/n)
# print(f'Lista de medias por tratamientos: {Xin}')

#* FACTOR DE CORRECCIÓN

#? C = SUM(Xij)^2 /k*n

sum = 0
for Xij in np.nditer(data):
    sum = sum + Xij # type: ignore
C = (pow(sum,2)) / (k*n)
# print(sum)
# print(f'El factor de correccion es: C = {C}')

#* SUMA DE CUADRADOS TOTALES

#? SCtot =  SUM(Xij^2) - C

SC = 0

for Xij in np.nditer(data):
    SC = SC + pow(Xij,2) # type: ignore
SCtot = SC - C
# print(f'La suma de cuadrados totales es: SCtot = {SCtot}')

#* SUMA DE CUADRADOS POR BLOQUES

#? SCbloques =  SUM((Tj)^2)/k - C

tj = 0
for Tj in Tnj:
    tj = tj + pow(Tj,2)
SCB = (tj/k) - C
# print(f'La suma de cuadrados por bloques es: SCB = {SCB}')

#* SUMA DE CUADRADOS POR TRATAMIENTOS

#? SCtratamientos =  SUM((Ti)^2)/n - C

ti = 0
for Ti in Tin:
    ti = ti + pow(Ti,2)
SCT = (ti/n) - C
# print(f'La suma de cuadrados por tratamientos es: SCT = {SCT}')

#* SUMA DE CUADRADOS RESIDUALES:

#? SCresiduales =  SC - SCB - SCT

SCres = SCtot - (SCB + SCT)
# print(f'La suma de cuadrados residual es: SCres = {SCres}')

#* ERROR CUADRATICO MEDIO BLOQUES

#? CMB = SCB/(n-1)

CMB = SCB/GLB
# print(f'El error cuadratico medio por bloques es: CMB = {CMB}')

#* ERROR CUADRATICO MEDIO TRATAMIENTOS

#? CMT = SCT/(k-1)

CMT = SCT/GLT
# print(f'El error cuadratico medio por tratamientos es: CMT = {CMT}')

#* ERROR CUADRATICO MEDIO RESIDUAL

#? CMres = SCres/(k-1)(n-1)

CMres = SCres/GLres
# print(f'El error cuadratico medio residual es: CMres = {CMres}')

#* RAZON DE VARIANZAS

#? RVtrat = CMTraramientos / CMresidual

RVtrat = CMT / CMres
# print(f'La razon de varianzas de tratamientos es: RVtratamientos = {RVtrat}')

#? RVbloques = CMBloques / CMresiduales

RVbloque = CMB / CMres
# print(f'La razon de varianzas de bloques es: RVbloques = {RVbloque}')


#'TABLA DE DATOS

import prettytable
from prettytable import PrettyTable

# Crear una tabla:
tabla_resultados = PrettyTable()

# Definir los encabezados de la tabla
tabla_resultados.field_names = ["Parámetro", "Valor"]

# Agregar los resultados a la tabla
tabla_resultados.add_row(["Tamaño total de la muestra (N)", N])
tabla_resultados.add_row(["Número de bloques (n)", n])
tabla_resultados.add_row(["Número de tratamientos (k)", k])
tabla_resultados.add_row(["Grados de libertad totales (GLtot)", GLtot])
tabla_resultados.add_row(["Grados de libertad de bloques (GLB)", GLB])
tabla_resultados.add_row(["Grados de libertad de tratamientos (GLT)", GLT])
tabla_resultados.add_row(["Grados de libertad residuales (GLres)", GLres])
tabla_resultados.add_row(["Factor de corrección (C)", C])
tabla_resultados.add_row(["Suma de cuadrados totales (SCtot)", SCtot])
tabla_resultados.add_row(["Suma de cuadrados por bloques (SCB)", SCB])
tabla_resultados.add_row(["Suma de cuadrados por tratamientos (SCT)", SCT])
tabla_resultados.add_row(["Suma de cuadrados residuales (SCres)", SCres])
tabla_resultados.add_row(["Error cuadrático medio por bloques (CMB)", CMB])
tabla_resultados.add_row(["Error cuadrático medio por tratamientos (CMT)", CMT])
tabla_resultados.add_row(["Error cuadrático medio residual (CMres)", CMres])
tabla_resultados.add_row(["Razón de varianzas (RVtratamiento)", RVtrat])
tabla_resultados.add_row(["Razón de varianzas (RVbloques)", RVbloque])

print(tabla_resultados)


#'TABLA ANOVA
#'GRAFICO DE DISTRIBUCION F CON PERCENTILES
