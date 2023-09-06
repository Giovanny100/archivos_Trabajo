'''
ENCAPSULAMIENTO: PERMITE RESTRINGIR O OCULTAR EL ACCESO A LOS DATOS DENTRO DE LA MISMA CLASE DEL MUNDO EXTERIOR (USUALMENTE SE MODIFICAN VIA METODOS DE LA MISMA CLASE).
'''

class Restaurante:
    def __init__(self,nombre,categoria,precio):
        self.nombre = nombre   #Por default los atributos estan guardados como Public (se pueden modificar en cualquier parte del codigo)
        self._categoria = categoria #Protected (agregar guion bajo en el atributo), sigue siendo podificable dentro de la misma clase.
        self.__precio = precio #Private (agregar doble guion bajo en el atributo), ya no puede ser accedido externamente, solo por medio de un metodo.

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, categoria: {self._categoria}, precio: {self.__precio}')


#Instanciar la clase:

restaurant = Restaurante('Pizzeria Mexico','Comida italiana', 50)
#print(restaurant.__precio) ya no se puede acceder a el atributo de esta forma
#Se uede modificar los valores de los atributos de la clase:
#restaurant.__precio = 60 #Tampoco se puede modificar de esta forma.
restaurant.mostrar_info()

#Se uede modificar los valores de los atributos de la clase:
#restaurant.__precio = 60 #Tampoco se puede modificar de esta forma.

restaurant2 = Restaurante('Hamburgesas py','Comida corrida',20)
#print(restaurant2.__precio) ya no se puede acceder a el atributo de esta forma

#Como se puede ver anterirormente logramos modificar el valor asignado de uno de los atributos del objeto, simplemente dandole otro valor.
#Con fines de mantener nuestro codigo restringido o oculto utilizamos el encapsulamiento: