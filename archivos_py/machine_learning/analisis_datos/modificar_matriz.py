import numpy as np

#* Cargar la matriz desde el archivo .npy:

matriz = np.load('C:/Users/mar_amez/Desktop/gio/archivos_py/matrices/ejemplo_lib.npy')

#* Modificar un elemento de la matriz (por ejemplo, el primer elemento de la primera fila):

nuevo_valor = 42

matriz[1, 3, 2] = nuevo_valor

#* Guardar la matriz modificada en el archivo .npy:
print(matriz)

np.save('ejemplo_lib.npy', matriz)
