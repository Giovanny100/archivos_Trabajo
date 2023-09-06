'''
LO QUE HACEMOS EN ESTE ARCHIVO ES ABRIR UN ARCHIVO PARA MOSTRAR SU CONTENIDO CON LA FUNCION WITH E ITERAR SOBRE EL MISMO
'''

def app():
    with open('archivo.txt') as archivo:
        for contenido in archivo:
        #PYTHON TIENE LA FUNCION removestrip (rstrip()) que quita los saltos de linea.
            print(contenido.rstrip())

app()