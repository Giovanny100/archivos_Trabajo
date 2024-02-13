

#*                                                   MODELO DE BLOQUES COMPLETAMENTE ALEATORIOS


#c NOMBRES DE VARIABLES:

#' Xijk = Observaciones individuales (elementos de la matriz)
#' N = Tamaño de nuestra total
#' n = Numero de tratamientos (Numero de filas por matriz) : Columnas
#' a = Niveles del factor A (Numero de matrices dentro de la matriz) : Filas
#' b = Niveles del factor B (Numero de columnas por matriz) : Dimención

#': GLtot = Grados de libertad totales
#': GLA = Grados de libertad factor A
#': GLB = Grados de libertad factor B
#': GLT = Grados de libertad tratamiento
#': GLres = Grados de libertad residuales

#': C = Factor de corrección
#' Tn = Totales por tratamiento
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

data = np.load('C:/Users/mar_amez/Desktop/gio/archivos_py/matrices/ejemplo_lib.npy')
print(data)

#* TAMAÑOS DE MUESTRA
#? N = Tamaño de nuestra total

N = 0
for Xijk in np.nditer(data):
    N = N + 1
print(f'Tamaño total de la muestra: N = {N}')

#* NUMERO DE TRATAMIENTOS Y NIVELES DE FACTORES A Y B
nivA, trat, nivB = data.shape

#? Niveles del fator A:
a = nivA

#? Niveles del fator B:
b = nivB

#? Numero de tratamientos:
n = trat

# print("Niveles del factor A:", nivA)
# print("Tratamientos", trat)
# print("Niveles del factor B:", nivB)

# #* GRADOS DE LIBERTAD

# #? DF(totales) = a*b*n - 1

GLtot = a*b*n - 1
print(f'Los grados de libertad totales son: GLtot = {GLtot}')

# #? DF(nivelesA) = a - 1

GLA = a - 1
print(f'Los grados de libertad de bloques son: GLA = {GLA}')
#? DF(nivelesB) = b - 1

GLB = b - 1
print(f'Los grados de libertad de bloques son: GLB = {GLB}')

#? DF(interaccionesAB) = (a - 1)(b - 1)

GLAB = (a - 1)*(b - 1)
print(f'Los grados de libertad de bloques son: GLAB = {GLAB}')

# #? DF(tratamientos) = ab - 1

GLT = (a*b) - 1
print(f'Los grados de libertad de tratamientos son: GLT = {GLT}')

#? DF(residuales) = a*b*(n - 1)

GLres = a*b*(n - 1)
print(f'Los grados de libertad residuales son: GLres = {GLres}')

#* TOTALES POR TRATAMIENTOS:

Tn = []
for xi in data:
    sumas = sum(xi)
    Tn.append(sumas)
print(f'Lista de totales por tratamientos: {Tn}')

#* MEDIAS POR TRATAMIENTOS

Xn = []
for Ti in Tn:
    Xn.append(Ti/n)
print(f'Lista de medias por bloques: {Xn}')

#* TOTALES POR NIVELES DE B
Tna = 0
for i in data:
    for j in i:
        Tna += j
print(f'Lista de totales por niveles de B: {Tna}')

#* MEDIAS POR NIVELES DE B
Xna = []
for Tj in Tna: # type: ignore
    Xna.append(Tj/(n*a))
print(f'Lista de medias por niveles de B: {Xna}')

#* TOTALES POR NIVELES DE A
#'AQUI ME QUDE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Tnb =  np.sum(data, axis = 0)
print(f'Lista de totales por niveles de A: {Tnb}')

# #* FACTOR DE CORRECCIÓN

# #? C = SUM(Xij)^2 /k*n

# sum = 0
# for Xij in np.nditer(data):
#     sum = sum + Xij
# C = (pow(sum,2)) / (k*n)
# # print(sum)
# # print(f'El factor de correccion es: C = {C}')

# #* SUMA DE CUADRADOS TOTALES

# #? SCtot =  SUM(Xij^2) - C

# SC = 0

# for Xij in np.nditer(data):
#     SC = SC + pow(Xij,2)
# SCtot = SC - C

# # print(f'La suma de cuadrados totales es: SCtot = {SCtot}')

# #* SUMA DE CUADRADOS POR BLOQUES

# #? SCbloques =  SUM((Tj)^2)/k - C

# tj = 0
# for Tj in Tnj:
#     tj = tj + pow(Tj,2)
# SCB = (tj/k) - C
# # print(f'La suma de cuadrados por bloques es: SCB = {SCB}')

# #* SUMA DE CUADRADOS POR TRATAMIENTOS

# #? SCtratamientos =  SUM((Ti)^2)/n - C

# ti = 0
# for Ti in Tin:
#     ti = ti + pow(Ti,2)
# SCT = (ti/n) - C
# # print(f'La suma de cuadrados por tratamientos es: SCT = {SCT}')

# #* SUMA DE CUADRADOS RESIDUALES:

# #? SCresiduales =  SC - SCB - SCT

# SCres = SCtot - (SCB + SCT)
# # print(f'La suma de cuadrados residual es: SCres = {SCres}')

# #* ERROR CUADRATICO MEDIO BLOQUES

# #? CMB = SCB/(n-1)

# CMB = SCB/GLB
# # print(f'El error cuadratico medio por bloques es: CMB = {CMB}')

# #* ERROR CUADRATICO MEDIO TRATAMIENTOS

# #? CMT = SCT/(k-1)

# CMT = SCT/GLT
# # print(f'El error cuadratico medio por tratamientos es: CMT = {CMT}')

# #* ERROR CUADRATICO MEDIO RESIDUAL

# #? CMres = SCres/(k-1)(n-1)

# CMres = SCres/GLres
# # print(f'El error cuadratico medio residual es: CMres = {CMres}')

# #* RAZON DE VARIANZAS

# #? RVtrat = CMTraramientos / CMresidual

# RVtrat = CMT / CMres
# # print(f'La razon de varianzas de tratamientos es: RVtratamientos = {RVtrat}')

# #? RVbloques = CMBloques / CMresiduales

# RVbloque = CMB / CMres
# # print(f'La razon de varianzas de bloques es: RVbloques = {RVbloque}')


# #'TABLA DE DATOS

# import prettytable
# from prettytable import PrettyTable

# # Crear una tabla:
# tabla_resultados = PrettyTable()

# #*  Definir los encabezados de la tabla:

# tabla_resultados.field_names = ["Parámetro", "Valor"]

# #* Agregar los resultados a la tabla

# tabla_resultados.add_row(["Tamaño total de la muestra (N)", N])

# # Agregar una fila de guiones para simular una línea horizontal
# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Número de bloques (n)", n])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Número de tratamientos (k)", k])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Grados de libertad totales (GLtot)", GLtot])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Grados de libertad de bloques (GLB)", GLB])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Grados de libertad de tratamientos (GLT)", GLT])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Grados de libertad residuales (GLres)", GLres])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Factor de corrección (C)", C])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Suma de cuadrados totales (SCtot)", SCtot])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Suma de cuadrados por bloques (SCB)", SCB])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Suma de cuadrados por tratamientos (SCT)", SCT])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Suma de cuadrados residuales (SCres)", SCres])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Error cuadrático medio por bloques (CMB)", CMB])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Error cuadrático medio por tratamientos (CMT)", CMT])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Error cuadrático medio residual (CMres)", CMres])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Razón de varianzas (RVtratamiento)", RVtrat])

# tabla_resultados.add_row(["-" * 90, "-" * 88])

# tabla_resultados.add_row(["Razón de varianzas (RVbloques)", RVbloque])

# print(tabla_resultados)

#'TABLA ANOVA
#'GRAFICO DE DISTRIBUCION F CON PERCENTILES