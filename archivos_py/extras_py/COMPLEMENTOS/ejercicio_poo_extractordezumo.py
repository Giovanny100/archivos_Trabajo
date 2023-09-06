'''
Se te da una clase Zumo, que tiene las propiedades nombre y capacidad.
Necesitas completar el código para permitir la adición de dos objetos Zumo, resultando en un nuevo objeto Zumo con la combinación de capacidad nombres de los dos zumos que han sido añadidos.
Por ejemplo, si añades un zumo de naranja con capacidad 1.0 y un zumo de manzana con capacidad 2.5 capacity, el zumo resultante debería tener:
nombre: Orange&Apple
capacidad: 3.5
Los nombres se han combinado usando un símbolo & .
Usa el metodo __add__ para definir un comportamiento personalizado para el operador + y devover el objeto resultante.
'''
class Zumo:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

#SE AGREGO EL METODO MAGICO (DUNDER): __add__ PARA DARLE LA FUNCIONALIDAD REQUERIDA DE LA CLASE:
    def __add__(self,otro):
        return Zumo(self.name + "&" + otro.name, self.capacity + otro.capacity)
a = Zumo('Orange', 1.5)
b = Zumo('Apple', 2.0)
result = a + b
print(result)

