'''
SE TE DA UN MARCO DE DATOS QUE INCLUYE LOS NOMBRES (NAMES) Y CLASIFICAIONES (RANKS) DE LA GENTE.

HAY QUE TOMAR UN RANGO COMO ENTRADA Y GENERAR EL CORRESPONDIENTE NOMBRE DE LA COLUMNA DEL DATAFRAME COMO SERIES.

TEN EN CUENTA QUE EL RANGO ES UN NUMERO ENTERO, POR LO QUE DEBERAS CONVERTIR LA ENTRADA DEL USUARIO EN UN NUMERO ENTERO.
'''
import pandas as pd
data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom', 'Harry'],
   'rank': [4, 1, 3, 5, 2, 6]
}
df = pd.DataFrame(data, index=data['name'])
print(df)

new_ranke = int(input())

print(df.iloc[new_ranke])


