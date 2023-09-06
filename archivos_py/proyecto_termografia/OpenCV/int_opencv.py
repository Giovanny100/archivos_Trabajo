'''
OpenCV (Open Source Computer Library) es una biblioteca informatica de codigo abierto ampliamente utilizada para el procesamiento de imagenes
y la vision por computadora
'''
# 1. Instalar open CV en el entorno de desarrollo:

# pip install opencv-python

# 2. Importar la libreria:
# Es importante considerar que para no presentar incomvenientes con el uso de la libreria es recomendable importar las librerias numpy y matplotlib

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# 3. Cargar una imagen desde el archivo:

# variable = cv2.imread('ruta')

#4. Mostrar imagen en una ventana:

#cv2.imshow('Titulo de la imagen',variable)

'''
Para mostrar la imagen con 'cv2.imshow' se debe tener en cuenta que solo abrira una ventana emergente que podria cerrarse rapidaemente si no esperas
una tecla, esta ventana solo se muestra mientras el programa está ejecutándose. Una vez que el programa termina de ejecutarse, la ventana de visualización
se cerrará automáticamente.
Si no esperas una tecla presionada antes de que el programa termine, la ventana de visualización se cerrará inmediatamente después de que se muestre. Esto
sucede porque la ventana está asociada al proceso del programa y se destruirá cuando el proceso finalice.
'''
#Para solucionar el anterior problema se puede usar lo siguiente:
# cv2.waitKey(0) es una funcion de la biblioteca que espera que el usuario presione cualquier tecla antes de continuar con la ejecucion del programa
#Ademas el numero que se da como argumento a la funcion es una contador de espera en milisegundos, pero si se da 0 se interpreta como que espere indefinidamente

# cv2.destroyAllWindows es una funcion de opencv para cerrar todas las ventanas que fueron abiertas por funciones como cv2.imshow(). Su objetivo principal es limpiar
# y cerrar todas las ventanas de visualización que pudieron haber sido creadas durante la ejecución del programa. Esta función es especialmente útil cuando has
# finalizado el proceso de visualización de imágenes y deseas asegurarte de que todas las ventanas se cierren correctamente.

# Ejemplo:

import cv2

img = cv2.imread('C:/Users/mar_amez/Desktop/gio/tesis_py/imagenes/istockphoto-689479038-612x612.jpg')

cv2.imshow('Deteccion de imagen y filtrado',img)

cv2.waitKey(0)  # Esperar a que se presione una tecla antes de cerrar la ventana

cv2.destroyAllWindows()  # Cerrar todas las ventanas abiertas por OpenCV

'''
Manipulacion Basica de Imagenes

Hay información de la imagen que se encuentra almacenada en tuplas tal como la siguiente (alto,ancho,color), es decir que la tupla devuelve numero de filas , columnas
y canales de color (si la imagen fuera a color), es util desenvolver las tuplas para poder utilizar sus valores en el codigo, como para redimesionar la imagen.
'''
#EJEMPLO DE REDIMENSIONAMIENTO DE IMAGEN:

# Obtener las dimensiones actuales de la imagen:

# alto, ancho = variable.shape[:2]

# Definir nuevas dimensiones:

# nuevo_alto = int(alto * 0.5)  # Reducción del 50% en la altura
# nuevo_ancho = int(ancho * 0.5)  # Reducción del 50% en el ancho

# REDIMENCIONAR LA IMAGEN:

# variable_redimensionada = cv2.resize(variable, (nuevo_ancho, nuevo_alto))

# Mostrar la imagen original y la redimensionada:

#cv2.imshow('Imagen Original', variable)
#cv2.imshow('Imagen Redimensionada', variable_redimensionada)

# CONVERTIR IMAGEN A ESCALA DE GRISES:

# img_grises = cv2.cvtColor(variable,cv2.COLOR_BGR2GRAY)


# Guardar una nueva imagen:

# cv2.imwrite("imagen_grises.jpg", imagen_grises)

'''
DETECCIÓN DE CONTORNOS

La umbralización (thresholding en inglés) es una técnica común utilizada en procesamiento de imágenes para convertir una imagen en escala de grises en una imagen
binaria. La imagen binaria consta solo de dos valores de píxeles posibles: blanco (representado por 1) y negro (representado por 0). La umbralización se basa en la
idea de establecer un umbral (umbral de intensidad) y clasificar los píxeles de acuerdo a si su intensidad está por encima o por debajo de ese umbral.

En el contexto de la detección de contornos, la umbralización es utilizada para resaltar los bordes y características de interés de la imagen original. Al convertir
la imagen en escala de grises en una imagen binaria, los bordes y contornos se vuelven más prominentes y fáciles de identificar.

Esta línea de código aplica umbralización a una imagen en escala de grises (imagen_grises) y produce una imagen binaria (imagen_binaria) con dos valores de píxeles
posibles: 0 (negro) o 255 (blanco).

Ahora, vamos a desglosar los componentes de esta línea de código:

ret: Es un valor que se devuelve como resultado de la función cv2.threshold(). Representa el umbral calculado automáticamente por la función, que puede ser útil en
algunas situaciones. Si no necesitas este valor, puedes ignorarlo.

imagen_binaria: Esta variable recibirá la imagen binaria resultante después de aplicar la umbralización.

cv2.threshold(imagen_grises, 127, 255, cv2.THRESH_BINARY): Aquí se llama a la función cv2.threshold() para aplicar la umbralización. Los argumentos son los siguientes:

imagen_grises: La imagen en escala de grises a la cual se aplicará la umbralización.

127: Valor umbral. Los píxeles con intensidad por encima de este valor se convertirán en blanco (255) y los píxeles por debajo de este valor se convertirán en negro (0).
255: Valor máximo a asignar a los píxeles que superen el umbral. En este caso, se establece a 255 para que los píxeles por encima del umbral sean blancos.
cv2.THRESH_BINARY: Este argumento indica el tipo de umbralización a aplicar. En este caso, se está utilizando la umbralización binaria, donde los píxeles por encima del
umbral se establecen en un valor máximo (255) y los píxeles por debajo se establecen en 0.

# Convertir la imagen a escala de grises:

# variable_grises = cv2.cvtColor(variable, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para obtener una imagen binaria:

# ret, variable_binaria = cv2.threshold(variable_grises, 127, 255, cv2.THRESH_BINARY)

Para la función de cv2.FindContours;
cv2.RETR_EXTERNAL: Este es un parámetro que determina el modo de recuperación de contornos. RETR_EXTERNAL significa que solo se recuperarán los contornos
externos (contornos que no están contenidos dentro de otros contornos). Otras opciones para este parámetro incluyen RETR_LIST, RETR_TREE, entre otros.

cv2.CHAIN_APPROX_SIMPLE: Este es otro parámetro que determina cómo se almacenan los puntos del contorno. CHAIN_APPROX_SIMPLE significa que solo se almacenan los puntos
extremos del contorno, lo que ahorra espacio en memoria. Otra opción es CHAIN_APPROX_NONE, que almacena todos los puntos del contorno.

contornos: Esta variable almacenará la lista de contornos encontrados en la imagen. Cada contorno es una matriz de puntos (coordenadas x, y) que representan la forma
del objeto.

jerarquia: Esta variable almacenará la información jerárquica de los contornos. La jerarquía describe cómo los contornos están organizados entre sí, si hay contornos
anidados, etc.

Para la funcion: cv2.drawContours()

Este es otro método de la biblioteca OpenCV que se utiliza para dibujar contornos en una imagen. Toma la imagen en la que deseas dibujar los contornos, la lista de
contornos que quieres dibujar, así como otros parámetros para especificar cómo se deben dibujar los contornos.

variable: Esta es la imagen en la que deseas dibujar los contornos. Debes proporcionar una variable que contenga la imagen en la que deseas realizar el dibujo.

contornos: Esta es la lista de contornos que deseas dibujar en la imagen. Normalmente, es la lista de contornos obtenidos utilizando cv2.findContours().

-1: El índice del contorno que deseas dibujar en esta llamada. El valor -1 significa que se dibujarán todos los contornos de la lista.

(0, 255, 0): Es el color en el que deseas dibujar los contornos. En este caso, (0, 255, 0) corresponde al color verde en el formato RGB.

2: El grosor del trazo utilizado para dibujar los contornos. En este caso, se utiliza un grosor de línea de 2 píxeles.

'''

# Encontrar contornos en la imagen binaria:

# contornos, jerarquia = cv2.findContours(variable_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en la imagen original:

# cv2.drawContours(variable, contornos, -1, (0, 255, 0), 2)

# Mostrar la imagen con contornos:

# cv2.imshow("Imagen con Contornos", variable)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
FILTRADO DE IMAGEN

'''

# # Aplicar un filtro de desenfoque
# imagen_desenfocada = cv2.GaussianBlur(imagen, (5, 5), 0)

# # Aplicar un filtro de detección de bordes
# imagen_bordes = cv2.Canny(imagen, 100, 200)

# # Mostrar la imagen con bordes detectados
# cv2.imshow("Imagen con Bordes", imagen_bordes)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
