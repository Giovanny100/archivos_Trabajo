'''
cv2.GaussianBlur(): Esta es una función de la biblioteca OpenCV que se utiliza para aplicar un filtro de desenfoque gaussiano a una imagen. El desenfoque gaussiano
es un método de suavizado que reduce el ruido y los detalles finos en una imagen.

imagen_desenfocada: Esta es la variable en la que se almacenará la imagen después de aplicar el desenfoque gaussiano.

img: Esta es la imagen original en la que deseas aplicar el desenfoque gaussiano. Debes proporcionar una variable que contenga la imagen en la que deseas
aplicar el filtro.

(5, 5): Este es el tamaño del kernel del filtro gaussiano. El kernel es una matriz utilizada para realizar operaciones de convolución en la imagen.
En este caso, (5, 5) especifica un kernel de tamaño 5x5. Cuanto mayor sea el tamaño del kernel, mayor será el efecto de suavizado.

0: Este es el valor de desviación estándar para el filtro gaussiano. Una desviación estándar de 0 indica que OpenCV calculará automáticamente la desviación estándar
basándose en el tamaño del kernel. Si proporcionas un valor positivo, ese valor se utilizará como desviación estándar.

EL RUIDO

En una imagen se refiere a las variaciones aleatorias e indeseadas en los valores de los píxeles que pueden ser causadas por diversas fuentes durante el proceso de
captura, transmisión o procesamiento de la imagen. Estas variaciones pueden introducirse debido a factores como la sensibilidad del sensor de la cámara,
la interferencia electromagnética, la compresión de datos, problemas en la óptica de la cámara, fluctuaciones eléctricas y otros factores externos.

El ruido puede manifestarse en diferentes formas, como pequeñas fluctuaciones de brillo o color en regiones homogéneas de la imagen, manchas aleatorias de píxeles
brillantes o oscuros, granulación en áreas uniformes, etc. Estas variaciones no están relacionadas con la información real de la escena que se captura, lo que puede
dificultar la interpretación correcta de la imagen y la realización de tareas de procesamiento posterior.

Existen varios tipos de ruido en las imágenes, incluidos:

Ruido Gaussiano: Se asemeja a una distribución gaussiana y es el tipo de ruido más común. Puede dar lugar a pequeñas variaciones de brillo en toda la imagen.

Ruido Sal y Pimienta: Causa la aparición de píxeles extremadamente brillantes (sal) o oscuros (pimienta) en la imagen, como si estuvieran esparcidos aleatoriamente.

Ruido Aleatorio: Es un ruido general que puede manifestarse en varias formas, como granulación o patrones de interferencia en la imagen.

Ruido de Cuantización: Se produce debido a la limitación en la representación de colores o niveles de gris en imágenes digitales, lo que puede llevar a la aparición
de bandas o distorsiones en transiciones suaves.

RUIDO GAUSSIANO

Piensa en el ruido gaussiano como el chisporroteo o el crujido que puedes escuchar en una llamada telefónica o en una transmisión de radio cuando la señal es débil.
Esas pequeñas fluctuaciones en el sonido son como el ruido gaussiano en las imágenes. Agrega una especie de "estática visual" a la imagen que puede hacer que parezca
más borrosa o menos nítida.

Matemáticas Simplificadas:

El ruido gaussiano se modela matemáticamente utilizando una distribución gaussiana, también conocida como distribución normal o campana de Gauss. Imagina que lanzas
un dado y anotas los resultados muchas veces. Luego, graficas esos resultados en un gráfico. La distribución que obtendrías se asemejaría a una curva suave con un pico
en el medio.

En una imagen, el ruido gaussiano significa que, en lugar de tener un valor de brillo exacto en cada píxel, hay pequeñas variaciones alrededor del valor esperado.
Estas variaciones siguen esa misma curva suave y tienen más probabilidades de ser pequeñas y menos probabilidades de ser grandes.

Aplicación Práctica:

En el procesamiento de imágenes, a veces deseamos reducir este ruido gaussiano, ya que puede dificultar la detección de bordes o detalles importantes en la imagen.
Aplicamos filtros, como el filtro de desenfoque gaussiano, que suaviza la imagen y "difumina" el ruido. Pero, ¡cuidado! Si aplicamos demasiado desenfoque, podemos
perder detalles importantes en la imagen.

En resumen, el ruido gaussiano es como un patrón suave de variación aleatoria que afecta los valores de brillo en una imagen. Entenderlo es importante para mejorar
y limpiar imágenes, especialmente cuando trabajamos en análisis o mejoramiento de imágenes. A medida que avanzas en tu comprensión, podrás explorar técnicas más
avanzadas y aplicaciones especializadas en procesamiento de imágenes y visión por computadora.

KERNEL (MASCARA O MATRIZ DE CONVOLUCION)

Las operaciones de convolución son un concepto fundamental en el procesamiento de señales y de imágenes. Se utilizan para combinar dos conjuntos de datos, como una
señal y un filtro, para obtener una nueva señal modificada. En el contexto del procesamiento de imágenes, la convolución se aplica para realizar diversas tareas,
como el suavizado, la detección de bordes y la mejora de imágenes.

En el contexto de procesamiento de imágenes, la convolución generalmente implica deslizar un pequeño kernel (también conocido como máscara o matriz de convolución)
sobre una imagen y realizar operaciones matemáticas en los píxeles que se encuentran bajo el área del kernel. Cada elemento del kernel tiene un peso asociado, y se
multiplica por el valor del píxel correspondiente en la imagen. Luego, los productos se suman y se coloca el resultado en la posición correspondiente en la nueva imagen.

La fórmula general de una operación de convolución en 2D es:


(I∗K)(x,y)=∑ i=−a-->a∑ j=−b-->b  [I(x−i,y−j)⋅K(i,j)]

Donde:

I es la imagen de entrada.
K es el kernel (máscara de convolución).
a y b son las mitades de las dimensiones del kernel en términos de filas y columnas.
(x,y) son las coordenadas del píxel en la imagen de salida.

Las operaciones de convolución tienen diversas aplicaciones en procesamiento de imágenes, como:

Suavizado (Blur): Utiliza un kernel de suavizado para reducir el ruido y las irregularidades en la imagen, creando una versión más suave de la imagen original.

Detección de Bordes: Emplea kernels que resaltan los cambios abruptos de intensidad en la imagen, lo que permite detectar bordes y características.

Realce de Características: Puede realzar ciertas características en la imagen, como resaltar detalles o mejorar áreas de interés.

Mejora de Imágenes: Mediante la aplicación de filtros específicos, se pueden mejorar ciertos aspectos de la imagen.

Las operaciones de convolución son esenciales en la mayoría de los algoritmos de procesamiento de imágenes y visión por computadora, ya que permiten transformar
y resaltar diferentes características en las imágenes.
'''

import cv2

img = cv2.imread('C:/GitHub/uas/ssam/public/images/gettyimages-499135687-612x612.jpg')

# Aplicar un filtro de desenfoque:

imagen_desenfocada = cv2.GaussianBlur(img, (5, 5), 0) #Los argumentos de la matriz kernel solo aceptan argumentos impares

cv2.imshow("Imagen Desenfocada", imagen_desenfocada)

# Aplicar un filtro de detección de bordes:

img_bordes = cv2.Canny(img, 100, 200)

# Mostrar la imagen con bordes detectados:

cv2.imshow("Imagen con Bordes", img_bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
