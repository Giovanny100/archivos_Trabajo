'''
POLIMORFISMO: HABILIDAD DE TENER DIFERENTES COMPORTAMIENTOS BASADO EN QUE SUBCLASE SE ESTA UTILIZANDO, RELACIONADO MUY ESTRECHAMENTE CON LA HERENCIA.

ES DECIR A VECES ENTRE CLASES QUE HEREDAN UNA MISMA LO QUE REQUERIMOS ES QUE ALGUNAS COSAS CAMBIEN, YA SEA EL NUMERO DE ATRIBUTOS U ALGUNA OTRA COSA.
'''
#En la clase padre no se agrega la clase alberca debido al primer pila r de la programacion (abstraccion-especificar solo lo necesario).
class Restaurante:
    def __init__(self,nombre,categoria,precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, categoria: {self.categoria}, precio: {self.precio}')

    def get_precio(self):
        print(self.precio)

    def set_precio(self,precio):
        self.precio = precio


#POLIMORFISMO 1.QUEREMOS IDENTIFICAR LOS HOTELES QUE TIENEN ALBERCA (CAMBIAR EL NUMERO DE ATRIBUTOS):
class Hotel(Restaurante):
    def __init__(self,nombre,categoria,precio,alberca):
        super().__init__(nombre,categoria,precio)
        self.alberca = alberca
#POLIMORFISMO 2. AGREGAR UN METODO QUE SOLO EXISTA EN HOTEL (AGREGAR UN NUEVO METODO PARA UNA SOLA CLASE):
    def get_alberca(self):
        return self.alberca
#POLIMORFISMO 3. SE QUIERE UTILIZAR EL MISMO METODO PERO CON DIFERENTE INFORMACION (REESCRIBIR UN METODO):
    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, categoria: {self.categoria}, precio: {self.precio}, Alberca: {self.alberca}')

hotel = Hotel('hotel gio','5 estrellas', 200, 'si')
hotel.mostrar_info()
alberca = hotel.get_alberca()
print(alberca)

