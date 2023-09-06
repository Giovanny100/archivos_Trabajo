'''
LOS METACARACTERES SON LOS QUE HACEN LAS EXPRECIONES REGULARES MAS POTENTES QUE LOS METODOS DE CADENAS NORMALES.

TE PERMITEN CREAR EXPRESIONES REGULARES QUE REPRECENTAN CONCEPTOS "UNA O MAS REPRETICIONES DE UNA VOCAL"

LA EXISTENCIA DE LOS METACARCTERES REPRECENTA UN PROBLEMA SI DECEAS CREAR UNA EXPRESION REGULAR (O REGEX) QUE CORRESPONDA A UN METACARACTER LITERAL, COMO POR EJEMPLO "$".

PUEDES HACER ESTO ESCAPANDO METACARACTERES COLOCANDO UNA BARRA INVERTIDA DELANTE DE ELLOS.

SIN EMBARGO ESTO PUEDE CAUSAR PROBLEMAS, YA QUE LAS BARRAS INVERTIDAS TIENEN UNA FUNCION DE ESCAPAR EN CADENAS NORMALES DE PYTHON.
ESTO SIGNIFICA COLOCAR TRES O CUATRO BARRAS INVERTIDAS SEGUIDAS PARA HACER TODOS LOS ESCAPES.

PARA EVITAR ESTO, UTILIZA UNA CADENA PURA, LA CUAL ES UNA CADENA NORMAL CON UNA "r" DELANTE DE ELLA.

EL PRIMER METACARACTER QUE OBSERVAMOS SERA EL PUNTO (.) 

ESTE COINCIDE CON CUALQUIER CARACTER EXCEPTO CON UNA NUEVA LINEA.
'''

from cgitb import grey
import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")


'''
TAMBIEN ESTAN LOS METACARACTERES ^ Y $. ESTOS COINCIDEN CON EL start Y EL END DE UNA CADENA RESPECTIVAMENTE.
'''

pattern1 = r"^gr.y$"
if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")

#El patron "^gr.y$" significa que la cadena deberia empezar con gr y luegho seguirlo con cualquier caracter excepto una nueva linea y terminar en "y".
