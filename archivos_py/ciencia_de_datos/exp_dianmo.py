import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carga la imagen en color utilizando OpenCV (para versiones >= 4.5.2)
imagen = cv2.imread("C:/Users/mar_amez/Desktop/GIO/TESIS/imagenes/iagua1_6.jpg", cv2.IMREAD_COLOR)

# Carga la imagen en color utilizando OpenCV (para versiones < 4.5.2)
# imagen = cv2.imread("C:/Users/mar_amez/Desktop/GIO/TESIS/imagenes/iagua1_6.jpg")

# Comprueba si la imagen se ha cargado correctamente
if imagen is not None:
    print("Imagen cargada exitosamente.")
else:
    print("No se pudo cargar la imagen.")

# Convierte la imagen de BGR a RGB (para mostrarla correctamente en Matplotlib)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Muestra la imagen utilizando Matplotlib
plt.imshow(imagen_rgb)
plt.axis('off')  # Desactiva los ejes para ocultarlos
plt.show()
