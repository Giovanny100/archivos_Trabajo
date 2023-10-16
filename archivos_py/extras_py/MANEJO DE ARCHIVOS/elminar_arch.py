
#' Para elminar una archivo se debe importar el modulo del sistema operativo y ejecutar la funcion os.remove()

import os
# os.remove('my_file.txt') #* Elimina el archivo

#' Para evitar recibir un error se puede comprobar si existey eliminarlo:

if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
else:
    print('The file does not exist')

#' Tambien se puede eliminar carpetas utilizando el metodo os.rmdir()

os.rmdir('Nombre de la carpeta')