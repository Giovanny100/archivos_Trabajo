from PIL import Image

# Cargar la imagen
image = Image.open('')

# Definir el tamaño deseado en píxeles (para 2.5 x 3 cm a 300 ppp)
desired_width = int(2.5 * 300)  # Ancho en píxeles
desired_height = int(3 * 300)   # Altura en píxeles

# Redimensionar la imagen
resized_image = image.resize((desired_width, desired_height), Image.ANTIALIAS)

# Guardar la imagen resultante
resized_image.save('foto_infantil_RMJC.jpg')
