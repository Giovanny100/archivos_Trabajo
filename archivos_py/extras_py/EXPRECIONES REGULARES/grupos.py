'''
UN GRUPO PUEDE SER CREADO AL COLOCAR UNA PARTE DE UNA EXPRESION REGULAR ENTRE PARENTESIS.
ESTO SIGNIFICA QUE UN GRUPO PUEDE SER PASADO COMO ARGUMENTO A METACARACTERES COMO * y ?
'''
# NO CORRE EL CODIGO ????
import re

pattern = r"agg(spam)*"

if re.match(pattern,"egg"):
    print("Match 1")

if re.match(pattern,"eggspamspamspamegg"):
    print("Match 2")

if re.match(pattern,"spam"):
    print("Match 3")

'''
EL CONTENIDO DE LOS GRUPOS EN UNA COINCIDENCIA PUEDE SER ACCEDIDO CON LA FUNCION GROUP.
UNA LLAMADA A GROUP(0) O GROUP() DEVUELVE TODA LA COINCIDENCIA.

UNA LLAMADA GROUP(n) DONDE n ES MAYOR QUE CERO, DEVUELVE EL n-ESIMO GRUPO DE LA IZQUIERDA.

EL METODO GROUPS() DEVUELVE TODOS LOS GRUPOS A PARTIR DEL 1.
'''

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")

if match:
    print(match.group()) #devuelve toda la coincidencia de la cadena
    print(match.group(0)) #devuelve toda la coincidencia de la cadena
    print(match.group(1)) #devuelve la coincidencia de la cadena desde el elemento uno que es bc
    print(match.group(2)) #devuelve la coincidencia de la cadena desde el elemento dos que es de.

'''
EXISTEN VARIAS CLASES DE GRUPOS ESPECIALES.
DOS UTILES SON LOS GRUPOS CON NOMBRE Y LOS GRUPOS QUE NO CAPTURAN.
LOS GRUPOS CON NOMBRE TIENEN UN FORMATO (? P<nombre>...), DONDE NOMBRE ES EL NOMBRE DEL GRUPO Y ... ES EL CONTENIDO. SE COMPORTAN EXACTAMENTE IGUAL QUE LOS GRUPOS
REGULARES EXCEPTO QUE PUEDEN SER ACCEDIDOS POR group(nombre) ADEMAS DE SU NUMERO in.
LOS GRUPOS QUE NO CAPTURAN TIENEN EL FORMATO (?:...). NO SON ACCESIBLES POR EL METODO GROUP, ASI QUE PUEDEN SER AGREGADAS A UNA EXPRESION REGULAR EXISTENTE SIN CAMBIAR
LA NUMERACION.
'''
import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())
