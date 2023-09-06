import numpy as np
import cv2

img = cv2.imread('C:/Users/mar_amez/Desktop/gio/tesis_py/imagenes/cropped-Logo-UNAM-Dorado-Square.png')

# Obtener las dimensiones actuales de la imagen:
alto, ancho = img.shape[:2]

# Definir nuevas dimensiones:
nuevo_alto = int(alto * 0.4)  # Reducción del 50% en la altura
nuevo_ancho = int(ancho * 0.4)  # Reducción del 50% en el ancho

# Redimensionar la imagen:
img_redimensionada = cv2.resize(img, (nuevo_ancho, nuevo_alto))

# Mostrar la imagen original y la redimensionada:
# cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen Redimensionada', img_redimensionada)

# Guardar la imagen redimensionada en el disco:
ruta_guardado = 'C:/Users/mar_amez/Desktop/gio/tesis_py/imagenes/cropped-Logo-UNAM-Dorado-Square.png'
cv2.imwrite("C:/Users/mar_amez/Desktop/gio/tesis_py/imagenes/cropped-Logo-UNAM-Dorado-Square.png", img_redimensionada)

cv2.waitKey(0)
cv2.destroyAllWindows()
