'''
LA SECUENCIA DE FIBONACCI CONSISTE EN QUE CADA NUMERO DE LA SECUENCIA ES LA SUMA DE LOS DOS NUMEROS QUE LA PRECEDEN.

POR EJEMPLO:

AQUI ESTA LA SECUENCIA DE FIBBONACI, PARA NUMEROS, EMPEZANDO POR 0:

0,1,1,2,3,5,8,13,21,34,55...

ESCRIBE UN CODIGO PARA TOMAR EL NUMERO POSITIVO N (LA VARIABLE NUM EN LA PANTALLA DEL CODIGO) COMO ENTRADA, CALCULA RECURSIVAMENTE Y SACA LOS PRIMEROS NUMEROS N DE LA SECUENCIA DE FIBONACCI
(EMPEZANDO POR CERO).

EJEMPLO DE ENTRADA:
6

EJEMPLO DE SALIDA:
0
1
1
2
3
5

SI ESTAS HACIENDO LA SECUENCIA DE FIBONACCI PARA N NUMEROS, DEBES USAR LA CONDICION n<=1 COMO CASO BASE. 
'''

num = int(input())

#Los primeros dos numeros de la sucesion de fibonaci son 0 y 1 por lo tanto:
def fibonacci(n):
    if n<=1:
        return n
#En caso de que se tengan numeros mayores a uno entonces debemos sumar los anteriores al numero de entrada, en este caso seria (n-1) y (n-2):
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Por ultimpo iteramos sobre el rango de numeros que se generarian para imprimir cada elemento y no solo el del termino que estamos dando:
for number in range(num):
    print(fibonacci(number))

