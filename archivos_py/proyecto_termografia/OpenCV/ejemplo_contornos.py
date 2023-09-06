'''
Este codigo remarca los contornos de la imagen con unas lineas verdes para posteriormente ser manipulado de alguna forma.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:/GitHub/uas/ssam/public/images/gettyimages-499135687-612x612.jpg")

cv2.imshow('Imagen original', img) # Esta linea debe ponerse antes de que se apliquen los cambios a la mima

img_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# A PARTIR DE AQUI SE TRABAJA EN RESALTAR LOS CONTORNOS CON LA IMAGEN EN GRISES:

# Aplicar umbralización para obtener una imagen binaria:

ret, img_binaria = cv2.threshold(img_grises, 100, 225, cv2.THRESH_BINARY)

cv2.imshow('imagen binaria', img_binaria)  # Muestra la imagen donde se aplican los cambios a binaria (blanco y negro)

# Encontrar contornos en la imagen binaria:

contornos, jerarquia = cv2.findContours(img_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en la imagen original:

cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)

# Mostrar la imagen con contornos:

cv2.imshow("Imagen con Contornos", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
