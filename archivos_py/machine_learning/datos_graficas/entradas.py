
#' Matriz (i,j,k) : i = Niveles Factor A , j = Fila dentro de A , k = Niveles Factor B

import numpy as np

#* FUNCIÓN PARA PEDIR VALORES DE ENTRADA DE LA MATRIZ:

def llenar_matriz_con_entradas(filas, columnas, dimensiones):
    matriz = np.zeros((filas, columnas, dimensiones))  # Crear una matriz de ceros con las dimensiones especificadas
    for i in range(filas):
        for j in range(columnas):
            for k in range(dimensiones):
                valor = float(input(f"Ingrese el valor para la posición ({i+1}, {j+1}, {k+1}):\r\n "))
                matriz[i][j][k] = valor
    return matriz

#* LLAMARA A LA FUNCIÓN:

def mostrar_matriz(matriz):
    print("La matriz es:")
    print(matriz)

#* DEFINIR LAS DIMENCIONES DE LA MATRIZ:

filas = 4
columnas = 5
dimensiones = 4

#* LLENARA LA MATRIZ CON LAS ENTRADAS:

matriz = llenar_matriz_con_entradas(filas, columnas, dimensiones)
mostrar_matriz(matriz)

np.save('Matriz generada.npy', matriz)

