'''
PRECIO DEL STOCK DADO POR UN TIKER
'''
import matplotlib.pyplot as plt
import yfinance as yf

data = yf.Ticker('TSLA')
print(data.history()) #esto dara el precio del stock en el ultimo mes

#Tambien podemos mencionar un periodo como parametro.

print(data.history(period = '1y'))

'''
COMO LA VARIABLE DATA ES UN DATAFRAME PODEMOS FACILMENTE GRAFICARLO.

GRAFIQUEMOS EL PRECIO DE CLOSE DE STOCK DE TESLA EL MES PASADO
'''

x = data.history()['Close']

x.plot()

plt.savefig('Close.png')