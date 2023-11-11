
#' Función para cambiar las barras invertidas por normales que admita el programa:

def ruta():
    ruta = input('Ingrese la ruta de acceso:\r\n')
    ruta_n = ruta.replace('\\', '/')
    print(ruta_n)

ruta()