import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Función para cargar y mostrar una imagen
def cargar_imagen():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg *.png *.gif")])
    if ruta_archivo:
        imagen = Image.open(ruta_archivo)
        imagen.thumbnail((400, 400))  # Ajusta el tamaño de la imagen para mostrarla en la interfaz
        foto = ImageTk.PhotoImage(imagen)
        etiqueta_imagen.config(image=foto)
        etiqueta_imagen.image = foto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Visor de Imágenes")

# Botón para cargar una imagen
boton_cargar = tk.Button(ventana, text="Cargar Imagen", command=cargar_imagen)
boton_cargar.pack(pady=10)

# Etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack()

# Iniciar la aplicación
ventana.mainloop()
