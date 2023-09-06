'''
AHORA PODEMOS ACCEDER A OTOS PARAMETROS FINANCIEROS.

POR EJEMPLO VAMOS A EXTRAER LOS DATOS  DE LAS GANANCIAS ESTIMADAS DE LA PAGINA "ANALISIS"
'''
import pandas as pd
import requests
import matplotlib.pyplot as plt

url_link = 'https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA'
r = requests.get(url_link,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})


data = pd.read_html(r.text)
print(data[0])

'''
USAMOS EL INDEICE CERO [0] YA QUE ES EL PRIMERO EN LA TABLA DE LA PAGINA.

AHORA PODEMOS ACCEDER A LA FILADE LA TABLA Avg. Estimate Y GRAFICARLO COMO UNA GRAFICA DE BARRAS.
'''
data = data[0]
data = data[data['Earnings Estimate'] == 'Avg. Estimate']
data.plot(kind = 'bar')
