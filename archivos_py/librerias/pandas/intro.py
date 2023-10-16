
#' PANDAS: (Panel Data) y sirve para trabajar con grandes cantidades de datos y hacer analisis estadistico

#' La arquitectura de pandas es simila a las de excel (fila-columna) pero aqui son Dataframe (estructura 2D)

#? Serie: Es como una columna en una tabla (matriz unidimensional) que contiene cualquier tipo de datos

import pandas as pd

#c Crear un diccionario (estructura de datos):

mydict = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

#c Convertirlo a un Dataframe (tabla de datos) con pandas:

myvar = pd.DataFrame(mydict) #* Crea dataframe (tabla de datos) del diccionario mydataset
# print(myvar)

#c Obtener la serie (columna) 'cars' de los valores del diccionario:

df_ser = pd.Series(mydict["cars"]) #* Tabla de datos de los valores con clave cars en el diccionario
# print(df_ser)

#? Etiquetas: Los valores de datos se etiquetan con sus propios indices

#c Se debe acceder cuando ya es una serie de datos

# print(df_ser[0]) #* Obtiene el primer dato de la serie cars

#c Localizar filas: Se usa la función loc() para devolver una o mas filas especificas

# print(myvar.loc[2]) #* Acceder a las propiedades del elemento con indice 2 del Dataframe

#c Tambien se puede solo acceder a un conjunto de elementos de la base de datos:

# print(myvar.loc[[0,1]]) #* Accede a los elementos con indice 0 y 1 del Dataframe

#'                                 NOMBRAR INDICES

#' Con el argumento index puedes nombrar tus propios indices

#c Agregar una lista de nombres para dar un nombre a cada fila en lugar de la numeración automatica:

df = pd.DataFrame(mydict,index = ['carro1', 'carro2','carro3']) #* Cambia indices 0,1,2 a carro#
# print(df)

#' Se puede usar el indice nombrado en el atributo loc() para devolver una fila especifica

#c Devolver carro3 a partir de ese nombre de indice:

print(df.loc['carro3']) #* En lugar de utilizar 0 usamos el nombre asignado con index()