'''
AHORA QUE SABEMOS COMO OBTENER PRECIO DE LAS ACCIONES (STOCKS), PODEMOS LLEVAR A A CABO CALCULOS Y ANALISIS.

COMENZAREMOS CALCULANDO EL RENDIMIENTO DIARIO DE LAS ACCIONES.

OBTENGAMOS EL PRECIO DE LAS ACCIONES PARA TESLA EL AÑO PASADO.

CON EL FIN DE CLCULAR EL RENDIMEINTO DIARIO, USAREMOS LA FUNCION pct_change() LA CUAL CALCULA EL PORCENTAJE DE CAMBIO ENTRE EL ACTUAL ELEMETO Y EL PREVIO.

LO USAREMOS SOBRE LA COLUMNA "Close":
'''
import matplotlib.pyplot as plt

#Esto es lo aprendido previamente para extraer los datos:
import yfinance as yf
import pandas as pd
# data = yf.Ticker('TSLA')
# price = data.history(period = '1d')

# print(price)



# Define el símbolo de la acción
symbol = "TSLA"

# Descarga los datos históricos de la acción
data = yf.download(symbol, start="2010-01-01", end="2023-05-30")

# Muestra los primeros 5 registros del DataFrame
print(data.head())

# Accede al precio de cierre de la acción
closing_price = data["Close"]
print(closing_price)



#A partir de aqui se obtiene el rendimieto diario:

# x = price['Close'].pct_change() #Esta funcion pertenence a Pandas
# print(x)

# '''
# PARA VISUALIZAR LOS RESULTADOS PODEMOS CREAR UN GRAFICO DEL RENDIMIETO DIARIO DE LAS ACCIONES:
# '''

# x.plot()
# plt.savefig('Rendimiento diario')

# #Podemos tambien hacer un histograma para ver la distribucion:
# #Es necesario arreglar las especificaciones del histograma para que se logre visualizar correctamente:

# import yfinance as yf
# import matplotlib.pyplot as plt

# data = yf.Ticker('TSLA')
# price = data.history(period='1y')

# x = price['Close'].pct_change()

# x.plot(kind='hist')

# plt.savefig('plot.png') # No grafica lo que necesito ya que toma ene ele eje x los años en lugar del intervalo -1, 1

# '''
# DESPUES DE ENTENDER COMO ESTAN DISTRIBUIDOS LOS RENDIMIENTOS, PODEMOS CLACUILAR LOS RETORNOS DE UNA INVERSION.

# POR ESO NECESITAMOS CALCULAR LOS RETORNOS ACUMULADOS, LO CUAL PUEDE SER CALCULADO USANDO LA FUNCION cumprod()
# '''

# returns = (x+1).cumprod()

# returns.plot()
# plt.savefig('Rendimientos.png') #no genera el histograma

x = 160.679993
