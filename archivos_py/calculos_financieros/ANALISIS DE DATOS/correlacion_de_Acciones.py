'''
CORRELACIONES

EN FINANZAS, CORRELACION ES UNA ESTADISTICA QUE MIDE EL GRADO EN QUE DOS VALORES SE ALEJAN ENTRE SI.

PODEMOS FACILMENTE CALCULAR LA CORRELACION ENTRE ACCIONES EN PYTHON, CON LA FUNCION corr()
'''

import yfinance as yf
import pandas as pd
import requests

url_link = 'https://finance.yahoo.com/quote/TSLA/profile'

r = requests.get(url_link,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

data = pd.read_html(r.text)
print(data[0])

data = yf.download("TSLA", start = '2020-01-01')

x = data['Close'].pct_change()

corr = x.corr()

print(corr)
