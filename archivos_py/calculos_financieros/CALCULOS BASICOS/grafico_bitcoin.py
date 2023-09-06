'''
1. CALCULA CUANTA INVERSION VALE LA PENA PARA CADA FIN DE AÑO USANDO EL PRECIO DADO EN EL CODIGO.

2. REALIZA UN GRAFICO PARA MOSTRAR CUANTO CAMBIA EL VALOR DE TU INVERSION DE 1000 EN UN AÑO.

PRIMERO CALCULA CUANTOS BITCOINS TENDRAS AL INICIO DIVIDIENDO SU INVERSIÓN POR EL COSTO DEL BITCOIN EN EL PRIMER AÑO (EL PRIMER ELEMENTO DEL ARREGLO QUE SE DA).
LUEGO MULTIPLICA EL ARREGLO ENTERO DE LOS PRECIOS POR ESE NUMERO PARA OBTENER EL VALOR DE CADA AÑO. USA np.multiply(array,number) PARA MULTIPLICAR UN ARREGLO POR
UN NÚMERO.
'''

#ANTERIRORMENTE:

import numpy as np
import numpy_financial as npf

#PRECIO DE 2018 A  2021:
bitcoin = [3869.47,7188.46,22203.31,29391.78]

print(np.std(bitcoin))


bitcoin_IRR = [-500000, 3869.47*10, 7188.46*10, 22203.31*10, 29391.78*10]
print(npf.irr(bitcoin_IRR))


#INVERSION INICIAL:
investment_ini = 1000

bitcoins_ini = investment_ini/bitcoin[0]
print(bitcoins_ini)
valor_anual = np.multiply(bitcoin,bitcoins_ini)
print(valor_anual)

#GRAFICO:

import matplotlib.pyplot as plt
años = [2018,2019,2020,2021]

plt.plot(años,valor_anual)
plt.savefig('Crecimiento de Inversion Anual')