'''
HERENCIA: TE PERMITE CREAR UNA CLASE (HIJO) QUE SEA UNA COPIA DE OTRA, AL HEREDAR UNA CLASE TENDRAS TODOS LOS METODOS Y ATRIBUTOS DE LA CLASE PADRE EN EL HIJO.

PODRAS MODIFICARLOS EN CASO DE SER NECESARIO.
'''
#? Por default los atributos estan guardados como Public (se pueden modificar en cualquier parte del codigo)
#? Protected (agregar guion bajo en el atributo), sigue siendo modificable dentro de la misma clase.
#? Private (agregar doble guion bajo en el atributo), ya no puede ser accedido externamente, solo por medio de un metodo.

class Restaurante:
    def __init__(self,nombre,categoria,precio):
        self.nombre = nombre
        self._categoria = categoria
        self.__precio = precio

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, categoria: {self._categoria}, precio: {self.__precio}')

#Usando getters y setters:
#Definir un metodo dentro de la misma clase que nos permita acceder a la variable encapsulada:
    def get_precio(self):
        print(self.__precio)
#Definir una metodo que nos permita agregar un valor a una variable encapsulada:
    def set_precio(self,precio):
        self.__precio = precio

#DEFINIMOS UNA NUEVA CLASE HIJO A LAS QUE HEREDMOS LA PADRE:

class Hotel(Restaurante):
    def __init__(self,nombre,categoria,precio):
        super().__init__(nombre,categoria,precio)

class Salas(Restaurante):
    def __init__(self,nomb,salas):
        self.nombre = nomb
        self.salas = salas

hotel = Hotel('hotel gio','5 estrellas', 200)
hotel.mostrar_info()
