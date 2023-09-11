import matplotlib.pyplot as plt
import numpy as np

class Graficos:
    def __init__(self, tipo, title, color, variable,static):
        self.tipo = tipo
        self.title = title
        self.color = color
        self.variables = variable
        self.data = {}
        self.static = static
    def datos(self):
        for var in self.variables:
            values = []
            while True:
                val = input(f'Introduzca el valor de {var} (o presione Enter para finalizar): ')
                if val == '':
                    break
                try:
                    values.append(float(val))
                except ValueError:
                    print("Valor no válido. Introduzca un número válido.")
            self.data[var] = values

    def estetica(self):
        data = float(input('Intoduzca los parametros de estetica:\r\n'))
# Ejemplo de uso
Grafico1 = Graficos('Lineas', 'Y vs X', 'Red', ['funcion', 'independiente'],[0,1])
Grafico1.datos()
Grafico1.estetica()


print("Datos ingresados:")
print(Grafico1.data)
