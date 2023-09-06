'''
DIRIJAMONOS A YAHOO FINANZAS, EL CUAL PROPORCIONA DATOS DE COMPAÑIAS, SUS RENDIMIENTOS Y PERFILES FINANCIEROS.

POR EJEMPLO AQUI ESTA LA PAGINA DEL PERFIL DE TESLA: https://fiannce.yahoo.com/quote/TSLA/profile

LA PRIMER TABLA ES UNA LISTA DE CLAVES EXCLUSIVAS. VAMOS A PASARLOS A UN DATAFRAME.
'''

import pandas as pd

#Este codigo dara un error ya que yahoo comprueba el solicitante y requiere un encabezado válido:
# data = pd.read_html('https://fiannce.yahoo.com/quote/TSLA/profile')

'''
WEB SCRAPING:
NECESITAMOS ESPECIFICAR EL ENCABEZADO DEL SOLICITANTE. PARA ESO USAREMOS LA LIBRERIA requests.

requests: ES UN ESTANDAR QUE SIRVE PARA HACER SOLICITUDES HTTP CUANDO SE ESTA DESARROYANDO EL LADO DE UN SERVIDOR DE UNA PAGINA WEB.

UN ENCABEZADO DEL SOLICITANTE ES USADO EN UN HTTP request PARA DAR INFORMACION SOBRE EL CONTEXTO REQUERIDO, DE MODO QUE EL SERVIDOR PUEDE ADAPTAR LA RESPUESTA.
DIMOS DATOS NAVEGADOR WEB ESTANDAR.
'''

import requests

url_link = 'https://finance.yahoo.com/quote/TSLA/profile'

r = requests.get(url_link,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

data = pd.read_html(r.text)
print(data[0])

# Usamos la libreria requests para obteber los datos y pasarlos a la funcion read_html()
