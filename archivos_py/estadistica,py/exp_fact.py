

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

data = np.load('C:/Users/mar_amez/Desktop/gio/archivos_py/matrices/matriz743.npy')
print(data)

#* TAMAÑOS DE MUESTRA
#? N = Tamaño de nuestra total

N = 0
for Xijk in np.nditer(data):
    N = N + 1
# print(f'Tamaño total de la muestra: N = {N}')

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
# print(f'Los grados de libertad totales son: GLtot = {GLtot}')

# #? DF(nivelesA) = a - 1

GLA = a - 1
# print(f'Los grados de libertad de bloques son: GLA = {GLA}')
#? DF(nivelesB) = b - 1

GLB = b - 1
# print(f'Los grados de libertad de bloques son: GLB = {GLB}')

#? DF(interaccionesAB) = (a - 1)(b - 1)

GLAB = (a - 1)*(b - 1)
# print(f'Los grados de libertad de bloques son: GLAB = {GLAB}')

# #? DF(tratamientos) = ab - 1

GLT = (a*b) - 1
# print(f'Los grados de libertad de tratamientos son: GLT = {GLT}')

#? DF(residuales) = a*b*(n - 1)

GLres = a*b*(n - 1)
# print(f'Los grados de libertad residuales son: GLres = {GLres}')

#* TOTAL DE TODOS LOS DATOS

Tijk = 0
for Xijk in np.nditer(data):
    Tijk += Xijk #type: ignore
# print('Total de datos:',Tijk)

#* TOTALES POR TRATAMIENTOS:

Tn = []
for xi in data:
    sumas = sum(xi)
    Tn.append(sumas)
# print(f'Lista de totales por tratamientos: {Tn}')

#* MEDIAS POR TRATAMIENTOS

Xn = []
for Ti in Tn:
    Xn.append(Ti/n)
# print(f'Lista de medias por bloques: {Xn}')

#* TOTALES POR NIVELES DE B
Tna = 0
for i in data:
    for j in i:
        Tna += j
# print(f'Lista de totales por niveles de B: {Tna}')

#* MEDIAS POR NIVELES DE B

Xna = []
for Tj in Tna: # type: ignore
    Xna.append(Tj/(n*a))
# print(f'Lista de medias por niveles de B: {Xna}')

#* TOTALES POR NIVELES DE A

Tnb = []
for i in data:
    Tnb.append(np.sum(i))
# print(f'Lista de totales por niveles de A: {Tnb}')

#* MEDIAS POR NIVELES DE A

Xnb = []
for Ti in Tnb:
    Xnb.append(Ti/(n*b))
# print(f'Lista de medias por niveles de A: {Xnb}')

# #* FACTOR DE CORRECCIÓN

# #? C = SUM(Xijk)^2 /a*b*n

C = (pow(Tijk,2)) / (a*b*n)
# print(f'El factor de correccion es: C = {C}')

# #* SUMA DE CUADRADOS TOTALES

# #? SCtot =  SUM(Xijk^2) - C

SC = 0

for Xijk in np.nditer(data):
    SC = SC + pow(Xijk,2) #type: ignore
SCtot = SC - C

# print(f'La suma de cuadrados totales es: SCtot = {SCtot}')

# #* SUMA DE CUADRADOS POR TRATAMIENTOS

# #? SCtratamientos =  SUM((Tij)^2)/n - C

sctr = 0
sc = []
for Tij in np.nditer(Tn):
    sc.append(np.sum(np.square(Tij)))

for sci in sc:
    sctr += sci
SCT = (sctr/n) - C
# print(f'La suma de cuadrados por tratamientos es: SCT = {SCT}')

#* SUMA DE CUADRADOS PARA FACTOR A

#? SCA=  SUM((Ti)^2)/an - C

ti = 0
for Tb in Tnb:
    ti = ti + pow(Tb,2)
SCA = (ti/(a*n)) - C
# print(f'La suma de cuadrados por niveles de A es: SCA = {SCA}')

#* SUMA DE CUADRADOS PARA FACTOR B

#? SCA=  SUM((Ti)^2)/an - C

tj = 0
for Ta in Tna: #type: ignore
    tj = tj + pow(Ta,2)
SCB = (tj/(b*n)) - C
# print(f'La suma de cuadrados por niveles de B es: SCB = {SCB}')

#* SUMA DE CUADRADOS RESIDUALES:

#? SCresiduales =  SC - SCT

SCres = SCtot - SCT
# print(f'La suma de cuadrados residual es: SCres = {SCres}')

#* SUMA DE CUADRADOS DE INTERACCIONES AB

#? SCAB = SCtrat - SCA - SCB

SCAB = SCT - SCA -SCB
# print('La suma de cuadrados para las interacciones AB es: SCAB =',SCAB)

#* ERROR CUADRATICO MEDIO FACTOR A

#? CMA = SCA/(a-1)

CMA = SCA/GLA
# print(f'El error cuadratico medio por factor A es: CMA = {CMA}')

#* ERROR CUADRATICO MEDIO FACTOR B

#? CMB = SCB/(b-1)

CMB = SCB/GLB
# print(f'El error cuadratico medio por factor B es: CMB = {CMB}')

# #* ERROR CUADRATICO MEDIO TRATAMIENTOS

# #? CMAB = SCAB/(a-1)(b-1)

CMAB = SCAB/GLAB
# print(f'El error cuadratico medio por interacciones AB es: CMAB = {CMAB}')

# #* ERROR CUADRATICO MEDIO TRATAMIENTOS

# #? CMT = SCT/(ab-1)

# CMT = SCT/GLT
# print(f'El error cuadratico medio por tratamientos es: CMT = {CMT}')

#* ERROR CUADRATICO MEDIO RESIDUAL

#? CMres = SCres/ab(n-1)

CMres = SCres/GLres
# print(f'El error cuadratico medio residual es: CMres = {CMres}')

#c **************************************************RAZON DE VARIANZAS*********************************************************************

#* RAZON DE VARIANZAS PARA FACTOR A

#? RVA = CMA / CMresidual

RVA = CMA / CMres
# print(f'La razon de varianzas del factor A: RVA = {RVA}')

#* RAZON DE VARIANZAS PARA EL FACTOR B

#? RVB = CMB / CMresiduales

RVB = CMB / CMres
# print(f'La razon de varianzas para el factor B es: RVB = {RVB}')

#* RAZON DE VARIANZAS PARA LAS INTERACCIONES AB

#? RVAB = CMAB / CMresiduales

RVAB = CMAB / CMres
# print(f'La razon de varianzas para las interacciones AB es: RVAB = {RVAB}')


#'TABLA DE DATOS

import prettytable
from prettytable import PrettyTable

# Crear una tabla:
tabla_resultados = PrettyTable()

# Definir los encabezados de la tabla:
tabla_resultados.field_names = ["Parámetro", "Valor"]

# Agregar los resultados a la tabla
tabla_resultados.add_row(["Tamaño total de la muestra (N)", N])
tabla_resultados.add_row(["Número de bloques (n)", n])
tabla_resultados.add_row(["Grados de libertad totales (GLtot)", GLtot])
tabla_resultados.add_row(["Grados de libertad del factor A (GLA)", GLA])
tabla_resultados.add_row(["Grados de libertad del factor B (GLB)", GLB])
tabla_resultados.add_row(["Grados de libertad de interacciones (GLAB)", GLAB])
tabla_resultados.add_row(["Grados de libertad de tratamientos (GLT)", GLT])
tabla_resultados.add_row(["Grados de libertad residuales (GLres)", GLres])
tabla_resultados.add_row(["Factor de corrección (C)", C])
tabla_resultados.add_row(["Suma de cuadrados totales (SCtot)", SCtot])
tabla_resultados.add_row(["Suma de cuadrados por bloques (SCA)", SCA])
tabla_resultados.add_row(["Suma de cuadrados por tratamientos (SCB)", SCB])
tabla_resultados.add_row(["Suma de cuadrados residuales (SCres)", SCres])
tabla_resultados.add_row(["Error cuadrático medio por bloques (CMA)", CMA])
tabla_resultados.add_row(["Error cuadrático medio por tratamientos (CMB)", CMB])
tabla_resultados.add_row(["Error cuadrático medio por interacciones (CMAB)", CMAB])
tabla_resultados.add_row(["Error cuadrático medio residual (CMres)", CMres])
tabla_resultados.add_row(["Razón de varianzas para el factor A (RVA)", RVA])
tabla_resultados.add_row(["Razón de varianzas para el factor B (RVB)", RVB])
tabla_resultados.add_row(["Razón de varianzas para las interacciones AB (RVAB)", RVAB])

# Imprimir la tabla
print(tabla_resultados)



#'TABLA ANOVA
#'GRAFICO DE DISTRIBUCION F CON PERCENTILES