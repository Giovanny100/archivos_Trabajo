import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m
import seaborn as sns

PandG_2023 = pd.read_csv("C:/Users/mar_amez/Downloads/LABP.csv")

print(PandG_2023) #Genera el dataframe de los datos importados de yahoo

#Si lo que queremo es solo el precio de cierre de la accion:

print(PandG_2023['Close'])

#Para graficar los datos:

plt.plot(PandG_2023['Close'])
plt.show()

#AÑOS ANTERIORES:

