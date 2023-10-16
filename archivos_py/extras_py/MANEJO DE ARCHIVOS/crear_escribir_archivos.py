
#' Este codigo crea una archivo .txt y lo pone en formato lectura, despues de crearlo se escribe sobre 20 lineas con el iterador

def app():

    with open('archivo.txt', 'w') as archivo:
        for i in range(0,20):
            archivo.write('Esta es la linea ' + str(i) + "\r\n")

#*Es por buena practica cerrar el archivo para evitar uso excesivo de memoria:
    archivo.close()

app()