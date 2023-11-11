import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#? La libreria sklearn se utiliza para importar datos utiles para machine learning:
from sklearn.datasets import load_diabetes

#? Crear la variable que guarde el cojunto de datos:
datos = load_diabetes()
print(datos.DESCR)

