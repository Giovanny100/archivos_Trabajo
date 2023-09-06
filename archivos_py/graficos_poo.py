import matplotlib.pyplot as plt
import numpy as np

class Graficos:
    def __init__(self, tipo, title, color, variables):
        self.tipo = tipo
        self.title = title
        self.color = color
        self.variables = variables
        self.data = {}

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

# Ejemplo de uso
Grafico1 = Graficos('Lineas', 'Y vs X', 'Red', ['funcion', 'independiente'])
Grafico1.datos()

print("Datos ingresados:")
print(Grafico1.data)
