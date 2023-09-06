'''
VAMOS A CREAR UN PRGORAMA QUE LE PREGUNTE A LOS USUARIOS COMO QUIEWREN NOMBRAR UNA PLAYLIST E IR AGREGANDO CANCIONES.

CUANDO SE CREA UNA APP LO IDEAL ES TENER UNA FUNCION PRINCIPAL LA CUAL LLAMAREMOS app()
'''

#Creamos una variable (diccionario vacio) fuera de la funcion principal ya que estaremos haciendo uso de ella constantemente:
playlist = {}

#Creamos una lista vacia de canciones la cual se va ir llenando como el usuario agrege informacion:
playlist["canciones"] = []


#FUNCION PRINCIPAL
def app():

#Agregamos playlist:
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿como deceas llamar la playlist? \n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False #cuando se da un nombre se desactiva el bucle
            #LLamar a la funcion para agregar canciones:
            agregar_canciones()

#Agreagar las canciones del usuario:
def agregar_canciones():
    agregar_cancion = True
    while agregar_cancion:
        #Preguntar al usuario la cancion que decean agregar:
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe X para dejar de agregar canciones \r\n'

        cancion = input(pregunta)
        if cancion == 'X':
            agregar_cancion = False
            mostrar_resumen()
        else:
            #Agregar las canciones a la playlist:
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'playlist: {nombre_playlist} \r\n')
    print('Canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()

