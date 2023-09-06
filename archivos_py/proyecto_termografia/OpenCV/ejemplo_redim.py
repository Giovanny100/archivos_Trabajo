import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('C:/Users/mar_amez/Desktop/gio/tesis_py/imagenes/istockphoto-689479038-612x612.jpg')

#* mostrar = cv2.imshow('Deteccion de imagen y filtrado',img)

# Obtener las dimensiones actuales de la imagen:

alto, ancho = img.shape[:2]

# Definir nuevas dimensiones:

nuevo_alto = int(alto * 2)  # Reducción del 50% en la altura
nuevo_ancho = int(ancho * 2)  # Reducción del 50% en el ancho

# Redimensionar la imagen:

img_redimensionada = cv2.resize(img, (nuevo_ancho, nuevo_alto))

# Mostrar la imagen original y la redimensionada:

cv2.imshow('Imagen Original', img)

cv2.imshow('Imagen Redimensionada', img_redimensionada)

cv2.waitKey(0)

cv2.destroyAllWindows()

