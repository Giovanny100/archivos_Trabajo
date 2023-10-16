
#' Python tiene varias funciones para crear,leer,actualizar y eliminar archivos

#c La funcion clave para manejar archivos en python es open()
#c La funcion open() toma dos argumentos open(filename, mode)
#c Hay 4 metodos diferentes para abrir un archivo:

#a "r" (read): Abre el archivo en modo lectura, dara error si el archivo no existe
#a "a" (append): Abre el archivo para agregarlo y si no exite lo crea
#a "w" (write): Abre el archivo en modo escritura, crea el archivo si no existe
#a "x" (crear): Crea el archivo especificado, devuelve error si no existe

#' Se puede especificar si el archivo debe manejarse en modo binario o texto

#a "t" (text): Modo texto
#a "b" (binary): Modo binario

#'Para abrir el archivo y leerlo basta con especificar el nombre

f = open('nuevo.txt','r')
# print(f.read())

#' Tambien se le puede pedir a la funcion read() que devuelva un numero especifico de caracteres pasandole el numero como argumento

# print(f.read(7))

#' Se puede pedir que lea las lineas con el metodo readline()
#c Se debe escribir el mismo codigo la cantidad de veces equivalente a las linas que se decea mostrar

# print(f.readline()) #* Devuelve la primer linea del texto
# print(f.readline()) #* Devuelve la segunda linea del texto
# print(f.readline()) #* Devuelve la tercera linea del texto

#c Recorrer el archvo linea por linea:

for x in f:
    print(x)

#c Es buena practica cerrar siempre el archivo cuando se termine de trabajar con el:

f.close()


