
#' Scipy nos proporciona una forma de interoperar con matlab
#' Scipy tiene el modulo scipy.io el cual tiene funciones para trabajar con matrices de matlab

#' EXPORTAR DATOS EN FORMATO MATLAB

#' La funcion savemat() sirve para exportar datos en formato de matlab

#a El metodo toma los siguientes parametros:

#a filename: El nombre del archivo para guardar los datos
#a mdic : Un diccionario que contiene los datos
#a do_compression : Un valor booleano que especifica si se comprime el resultado o no (False por default)

# from scipy import io
# import numpy as np

# arr = np.arange(10)

# io.savemat('arr.mat', {"vec": arr})

#' IMPORTAR DATOS EN FORMATO MATLAB

#'La loadmat()función nos permite importar datos desde un archivo Matlab.

#'La función toma un parámetro requerido:

#a filename : el nombre del archivo de los datos guardados.

#' Devolverá una matriz estructurada cuyas claves son los nombres de las variables y los valores correspondientes
#' son los valores de las variables.

#c Importar la matriz del siguiente archivo con formato matlab:

# from scipy import io
# import numpy as np
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# #c Export:
# io.savemat('arr.mat', {"vec": arr})

# #c Import:
# mydata = io.loadmat('arr.mat')
# print(mydata)

