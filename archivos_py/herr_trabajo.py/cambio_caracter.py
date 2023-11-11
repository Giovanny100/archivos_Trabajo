
#* Crear un programa Python para procesar archivos de Word:

def change_charter(input_text):
    # Reemplaza todas las instancias de "?" con "!"
    modified_text = input_text.replace("#?", False)
    return modified_text

if __name__ == "__main__":
    input_text = """
AQUI VA EL TEXTO :)
"""

    modified_text = change_charter(input_text)

    print("\nTexto modificado:")
    print(modified_text)
