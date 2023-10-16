
#' Para escribir en un archivo ya existente se debe pasar una argumento a la funcion open()

#a "a" (agregar): Se agregara al final del archivo
#a "w" (escribir): Sobreescribira cualquier contenido existente

f = open('nuevo.txt', 'a') #* Abre el archivo y agrega contenido
f.write('\n Esta es una nueva linea del archivo')
f.close()

f = open("nuevo.txt", "r")
print(f.read())

#' Se usa el metodo open() con alguno de los siguientes parametros

#a "w" (escribir):Creara un archivo si el especificado no existe
#a "x" (Crear): Creara un archivo y devuelve error si ya existe
#a "a" (Agregar): Creara un archivo si el especificado no existe

#c Crear un archivo:

g = open('my_file.txt', 'x') #* Creara un archivo vacio
