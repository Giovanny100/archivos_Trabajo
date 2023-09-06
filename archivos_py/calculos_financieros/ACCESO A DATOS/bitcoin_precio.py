'''
EL PRECIO DE BITCOIN PUEDE ENCONTRARSE EN YAHOO FINANZAS USANDO EL TICKER 'BTC-USD'

1. IMPORTA yfinance Y CAMBIA EL CODIGO PARA OBTENER EL PRECIO REAL DE BITCOIN DESSDE YAHOO FINANCE EN EL UNTIMO AÑO (period = 1y)

2. CALCULA CUAL SERA EL VALOR CADA DIA SI SE INVIRTIO 1000 AL INICIO DEL PERIODO.

3. HACER UN GRAFICO QUE MUESTRE LOS CAMBIOS DE VALOR DE LA INVERSION.

CONSEJO:

CAMBIA EL CODIGO DE FORMA QUE LOS DATOS SE OBTENGAN DE YAHOO FINANCE

NNO NECESECIAS TRABAJAR CON EL ARREGLO INICIAL QUE SE DABA AL INICIO DEL PROYECTO

ESTE ES UN EJEMPLO DE COMO DEBERIAS OBTENER DATOS COMO UN ARREGLO:
'''

#Usar el siguiente codigo para remplazar la parte que fue creada inicialemente del arreglo de bitcoin:
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.Ticker('BTC-USD')

x = data.history('1y')['Close']

inv_ini = 1000

bitcoin_ini =  inv_ini/x[0]

crecimiento = np.multiply(bitcoin_ini,x)

plt.plot(crecimiento)
plt.savefig('Aumento de inversion BITCOIN.png')


