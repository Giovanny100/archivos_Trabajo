'''
SE DA UN DICCIONARIO QUE CONTIENE NOMBRES Y NUMEROS DE PERSONAS.

NECESITAS CREAR UN DATAFRAME DEL DICCIONARIO Y AÑADAE UN INDICE, QUE DEBERIA SER LOS VALORES DEL NOMBRE.

A CONTINUACION SE TOMA UN NOMBRE DE LA ENTRADA DEL USUARIO Y GENERA LA FILA EN EL DATAFRAME QUE CORRESPONDE A ESA FILA.

USA loc. PARA ENCONTRAR LA FILA ESPECIFICADA.
'''

import pandas as pd

data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
   'number': ['1234', '5678', '2222', '1111', '0909']
}

data_frame = pd.DataFrame(data)

indice = pd.DataFrame(data, index=['James', 'Billy', 'Bob', 'Amy', 'Tom'])

nombre = input()

print(indice.loc[nombre])