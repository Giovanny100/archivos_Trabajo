
#* Crear un programa Python para procesar archivos de Word:

def change_charter(input_text):
    # Reemplaza todas las instancias de "?" con "!"
    modified_text = input_text.replace("#", "#'")
    return modified_text

if __name__ == "__main__":
    input_text = """
# enumerate(lista_sumas, start=1): La función enumerate toma una secuencia (en este caso, lista_sumas) y devuelve tuplas que consisten en un índice y un valor
# correspondiente. El argumento start=1 se utiliza para especificar el valor inicial del índice (por defecto es 0, pero aquí se inicia en 1).

# for i, valor in ...: Desempaqueta las tuplas generadas por enumerate en las variables i y valor. i es el índice (1, 2, 3, ...) y valor es el valor
# correspondiente en lista_sumas.

# Entonces, en resumen, la línea for i, valor in enumerate(lista_sumas, start=1): significa que estás iterando sobre los elementos de lista_sumas, pero también
# obteniendo el índice de cada elemento empezando desde 1 en lugar de 0. Esto es útil para construir nombres de variables como T1, T2, etc. en el siguiente bloque
# del código.
"""

    modified_text = change_charter(input_text)

    print("\nTexto modificado:")
    print(modified_text)
