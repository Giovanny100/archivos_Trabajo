'''
El siguiente codigo da el reverso de un numero
'''


#*Será útil cuando se requira determinar si el numero de entrada es un palindromo (Capicúa), es decir que se lea igual en ambas direcciones:

#?Pedir la entrada del usuario (sera el número que se quiere voltear)
num = int (input('Ingrese el numero: \r\n'))

#? Esta variable es la que se encargara de llevar la suma del numero que se imprimira al final
#? Inicialmnte es cero para que pueda tomar solo el resultado de la operación de x
res = 0

#? El bucle tiene como condicion hasta que la division de n entre 10 sea positivo osea que sea un numero mayor que 10
while num > 0:
    x = num % 10  #?Se almacena en x el ultimo numero de la cifra es decir el residuo de la division de nuestro numero entre 10
    res = res*10 + x #? Se asigna un nuevo valor a la variable res que que sera el numero obtenido mas cero inicialmente despues ira multiplicando los mueros anteriores x 10
    num = num // 10 #? Se asigna un nuevo valor a la variable num que sera la parte entera del cociente entre 10 y se alimentara de nuevo al bucle hasta que no haya parte entera
print(res)
