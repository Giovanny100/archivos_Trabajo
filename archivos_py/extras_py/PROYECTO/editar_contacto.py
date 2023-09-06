'''
CRUD: Cread Read Update Delete (crear,leer,actualizar,borrar)

TODAS LAS APPS DE ESCRITORIO, WEB O MOVIL DEBEN TENER ESAS OPCIONES DISPONIBLES

PARA CREAR EL CODIGO CONDICIONAL DE CADA OPCION OCUPAREMOS WHILE
'''

import os  #Libreria para manejar archivos

CARPETA = 'contactos/' #Creamos carpeta de contactos con mayusculas porque de esa forma la indicamos constante para otros programadores.
EXTENSION = '.txt' #Extension de archvios

#Contactos:
class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria



def app():

    #Revisa si la carpeta existe:
    crear_directorio()

    #Muestra el menu de opciones:

    mostrar_menu()

    #Preguntar al usuario que decea realizar:
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion:\r\n')
        opcion = int(opcion)
        #Ejecutar las opciones:
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            borrar_contacto()
            preguntar = False
        else:
            print('opcion invalida intente de nuevo')

def borrar_contacto():
    nombre = input('Selecciona el contacto que decea elminar:\r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Elminado correctamente')
    except:
        print('No existe ese contacto')

    #Reiniciar la app:
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que decea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion delcontacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

    #einciciar la app:
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:

        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos:
                print(linea.rstrip())
            #Imprime un separador entre contactos:
            print('\r\n')

def editar_contacto():
    print('Escrube el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que decea editar\r\n')

    #Validar si el archivo ya existe antes de editarlo:
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            #Agregar resto de los campos:
            nombre_contacto = input('Agrega el nuevo nombre:\r\n')
            telefono_contacto = input('Agrega el nuevo telefono:\r\n')
            categoria_contacto = input('Agrega la nueva categoria: \r\n')

            #Instanciar:
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

            #Escribir en el archivo:
            archivo.write('Nombre' + contacto.nombre + '\r\n')
            archivo.write('Telfono:' + contacto.telefono + '\r\n')
            archivo.write('Categoria:' + contacto.categoria + '\r\n')
        #Renombrar el archivo:
        os.rename(CARPETA + nombre_anterior + EXTENSION,CARPETA + nombre_contacto + EXTENSION)

              #Mostrar mensaje de exito:
        print('\r\n Contacto editado correctamente \r\n')

    else:
        print('Ese contacto no existe')

    #Reiniciar app:
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto:')
    nombre_contacto = input('Nombre del contacto: \r\n')

    #Validar si el archivo ya existe antes de crearlo:
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo: #Permite crear o abrir el archivo sin necesidad de estarlo cerrando constantemente
            #Llenando el resto de los campos de contactos:
            telefono_contacto = input('Agrega el telefono:\r\n')
            categoria_contacto = input('Categoria Contacto: \r\n')

            #Instanciar la clase:
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

            #Escribir en el archivo:
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

    else:
        print('Ese contacto ya existe')

        #Reiniciar la app:
        app()

        #Mostrar mensaje de exito:
        print('\r\n Contacto creado correctamente \r\n')

def mostrar_menu():
    print('Seleccionar del menu lo que decea hacer:')
    print('1. Agregar un nuevo contacto') #Cread (Crear)
    print('2.Editar contacto') #Update(actualizar)
    print('3.Ver contactos') #Read (leer)
    print('4.Buscar contacto')
    print('5.Eliminar contacto') #Delate (borrar)


def crear_directorio():
    #os.path sirve para verificar si la ruta de un archivo existe o no
    if not os.path.exists(CARPETA): #con esto pedimos que si el archivo no existe lo cree
        #makedirs sircve para crear un directorio de manera recusrsiva (si falta algun directorio este los creara)
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()