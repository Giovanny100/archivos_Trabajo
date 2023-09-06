'''
DADO UN  TEXTO COMO ENTRADA,ENCUENTRA Y SACA LA PALABRA MAS LARGA.

PUEDES LLAMAR AL METODO split("") QUE DEVUELVE UNA LISTA DE PALABRAS DE LA CADENA.
'''

txt = input()
#Aqui comienza nuestro codigo:
#Creamos una lista de las palabras que contiene la cadena con el metodo split:
palabras = txt.split()

#Creamos otra lista vacia para ir agregando los valores de los tamaños de cada palabra:
letras = []

#Iteramos en la lista de palabras para sacar sus tamaños con len y agregarlos a la lista vacia letras:
for p in palabras:
    tamaños = len(p)
    letras.append(tamaños)

#Otra vez tenemos que iterar para esta ves darle la condicion con  que va a comparar en nuestra primer lista:
#Se condiciona a que imprima solo la palabra p de la lista de palabras solo si el tamaño de la palabra p es igual al valor maximo de los tamaños de la lista de letras:
for p in palabras:
    if len(p) == max(letras):
        print(p) 