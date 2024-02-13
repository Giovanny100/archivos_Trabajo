import numpy as np

#' Crear matriz de datos

def llenar_matriz_con_entradas(filas, columnas, dimensiones):
    matriz = np.zeros((filas, columnas, dimensiones))  #* Crear una matriz de ceros con las dimensiones especificadas
    for i in range(filas):
        for j in range(columnas):
            for k in range(dimensiones):
                valor = float(input(f"Ingrese el valor para la posición ({i+1}, {j+1}, {k+1}):\r\n "))
                matriz[i][j][k] = valor
    return matriz

def mostrar_matriz(matriz):
    print("La matriz es:")
    print(matriz)

#* Definir las dimensiones de la matriz

nivelesA = 3
tratamientos = 4
nivelesB = 3

#* Llenar la matriz con las entradas proporcionadas

matriz = llenar_matriz_con_entradas(nivelesA, tratamientos, nivelesB)
mostrar_matriz(matriz)

#* Luego de generar la matriz, guardarla en un archivo utilizando np.save:

np.save("matriz741.npy", matriz)

#*  Obtener el número de filas, columnas y dimensiones:

nivelesA, tratamientos, nivelesB = matriz.shape

print("Niveles del factor A:", nivelesA)
print("Numero de tratamientos:", tratamientos)
print("Niveles del factor B:", nivelesB)