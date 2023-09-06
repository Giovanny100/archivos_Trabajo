'''
Ahora que sabemos como llevar a cabo calculos financieros basicos observemoslo en un grafico.

Python tiene una paqueteria llamada matplotlib, la cual incluye una subpaqueteria llamada pyplot usada para crear graficos.
'''

import matplotlib.pyplot as plt

'''
Asumiremos que tenemos los datos de ingresos de una empresa en  5 meses en un arreglo.

Queremos un grafico grafico de visualizacion de los datos de ingresos.

Para hacer eso necesitamos simplemente llamar la funcion plot en nuestros datos.
'''

rev = [18000,25000,20000,45000,19500]

plt.plot(rev)

plt.savefig('plot1.png')

'''
LA FUNCION plot() TAMBIEN PUEDE TOMAR VALORES PARA AMBOS EJES X,Y.
AGREGRMOS EL NOMBRE DE LOS MESES EN EL EJE HORIZONTAL
'''

rev = [18000,25000,20000,45000,19500]

meses = ['Junio', 'Julio','Agosto','Septiembre', 'Octubre']

plt.plot(meses,rev)

plt.savefig('plot2.png')