import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#? La libreria sklearn se utiliza para importar datos utiles para machine learning:
from sklearn.datasets import load_diabetes

#? Crear la variable que guarde el cojunto de datos:
datos = load_diabetes()
print(datos)
#? Crear un DataFrame de pandas con los datos:
df = pd.DataFrame(data = datos.data, columns = datos.feature_names)
print(df)
#?  Añadir la variable objetivo al DataFrame:
df['target'] = datos.target

#? Guardar el DataFrame en un archivo Excel:
df.to_excel('diabetes_dataset.xlsx', index=False)