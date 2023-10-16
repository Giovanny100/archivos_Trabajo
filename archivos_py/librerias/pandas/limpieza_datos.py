
#' LIMPIEZA DE DATOS

#' Se refiere a arreglar datos no deseados en tu cojunto de datos (eliminar datos)

#' Datos no deceados pueden ser:

#a Celdas vacias
#a Datos con un formato no adecuado
#a Datos erroroneos
#a Datos duplicados

#' Celdas vacias: Pueden darte un resultado erroneo cuando haces analisis de datos
#' Remover esas celdas vacias resulta no afectar cuando se trabaja con ciencia de datos o big data

#c Devolver el DataFrame sin celdas vacias:

import pandas as pd

df = pd.read_csv('C:/Users/mar_amez/Desktop/gio/archivos_py/mi_archivo.csv')

# new_df = df.dropna() #* Creamos un DF que elimina los datos que tienen celdas vacias

# print(new_df.to_string())

#' Si lo que se quiere es modificar elarchivo original se puede utilizar como argumento: inplace = True

# df.dropna(inplace = True) #* Se esta modificando el dataframe original (elmina celdas vacias)

# print(df.to_string())

#'Remplazar valores vacios

#'Otra forma de tratar con celdas vacias es insertar un nuevo valor
#' El metodo fillna permite remplazar las celdas vacias con un nuevo valor

# df.fillna(130, inplace = True) #* Sustituye celdas vacioas con valor 130

# print(df.to_string())

#' REMPLAZAR UTILIZANDO MEDIA, MEDIANA Y MODA

#' Pandas usa los metodos mean(),median(), y moda() para calcular los valores respectivos para una columna especifica

#c Calcular la media y remplazar cuyalquier valor vacio con ella

media = df['Calories'].mean()

df['Calories'].fillna(media, inplace = True) #* Se sustituyeron valores celdas vacias 18 y 28 con el valor de media
# print(df.to_string())

#' Esto tambien se puede hacer con la median y moda:

# mediana = df["Calories"].median()
# moda = df["Calories"].moda()

#' Limpiar datos con formato erroneo

#' Se puede utilizar el metodo to_datetime() para corregir el formato de las fechas

df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())

#' Por ultimo podemos remover filas utilizando el metodo dropna()

#c Elimine filas con un valor NULL en la columna "Fecha":

# df.dropna(subset=['Date'], inplace = True)

#'Información incorrecta

#' Los "datos incorrectos" no tienen por qué ser "celdas vacías" o "formato incorrecto", simplemente pueden ser
#' incorrectos, como si alguien registrara "199" en lugar de "1,99".

#' A veces puedes detectar datos incorrectos al observar el conjunto de datos, porque tienes una expectativa de
#' lo que debería ser.

#' Si echa un vistazo a nuestro conjunto de datos, podrá ver que en la fila 7, la duración es 450, pero para
#' todas las demás filas la duración está entre 30 y 60.

#'No tiene por qué estar mal, pero teniendo en cuenta que se trata del conjunto de datos de las sesiones de
#' entrenamiento de alguien, concluimos con el hecho de que esta persona no hizo ejercicio en 450 minutos.

#c En nuestro ejemplo, lo más probable es que se trate de un error tipográfico y el valor debería ser "45"
#c  en lugar de "450", y podríamos simplemente insertar "45" en la fila 7:

#c Establecer 'Duration' = 45 en la fila 7:

df. loc[7, 'Duration'] = 45

#' Para reemplazar datos incorrectos en conjuntos de datos más grandes, puede crear algunas reglas, por ejemplo,
#' establecer algunos límites para los valores legales y reemplazar cualquier valor que esté fuera de los límites

#c Recorra todos los valores en la columna "Duración"
#c Si el valor es superior a 120, configúrelo en 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())