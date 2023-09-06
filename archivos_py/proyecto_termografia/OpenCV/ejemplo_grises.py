import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/mar_amez/Desktop/gio/tesis_py/imagenes/istockphoto-689479038-612x612.jpg')

img_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagen en escala de grises',img_grises)

cv2.waitKey(0)

cv2.destroyAllWindows()