'''
LOS METODOS GETTERS Y SETTERS SE UTIIZAN PARA PODER ACCEDER A UNA VARIABLE QUE FUE ENCAPSULADA COMO PRIVATE

GETTER: OBTIENE UN VALOR

SETTER: COLOCA O AGREGA UN VALOR
'''

class Restaurante:
    def __init__(self,nombre,categoria,precio):
        self.nombre = nombre   #Por default los atributos estan guardados como Public (se pueden modificar en cualquier parte del codigo)
        self._categoria = categoria #Protected (agregar guion bajo en el atributo), sigue siendo podificable dentro de la misma clase.
        self.__precio = precio #Private (agregar doble guion bajo en el atributo), ya no puede ser accedido externamente, solo por medio de un metodo.

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, categoria: {self._categoria}, precio: {self.__precio}')

#Usando getters y setters:
#Definir un metodo dentro de la misma clase que nos permita acceder a la variable encapsulada:
    def get_precio(self):
        print(self.__precio)
#Definir una metodo que nos permita agregar un valor a una variable encapsulada:
    def set_precio(self,precio):
        self.__precio = precio


restaurant = Restaurante('Pizzeria Mexico','Comida italiana', 50) #Instancia de clase para crear un objeto con los atributos
restaurant.mostrar_info() #Muestra la informacion que fue definida inicialemente en la clase.
restaurant.set_precio(80) #Coloca o modifica el valor de un atributo (variable) que fue encapsulado como Private.
restaurant.get_precio() #Obtiene o accede a el valor encapsulado de la clase.

restaurant2 = Restaurante('Hamburgesas py','Comida corrida',20)
restaurant2.mostrar_info()
restaurant2.set_precio(52)
restaurant2.get_precio()


