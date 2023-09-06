'''
EXTRAER DATOS DE YAHOO REQUIERE TRABJO MANUAL,INCLUYENDO AGREGAR LA URL, HACIENDO EL request Y USANDO LA FUNCION read_html().

OTRA FORMA DE OBTENER DATOS FINANCIEROS DE YAHOO ES USANDO LA LIBRERIA yfinance.

FUE CREADA PARA DAR UN ACCESO FACIL A LOS DATOS FINANCIEROS, SIN NECESIDAD DE TRABAJO MANUAL.
'''

import yfinance as yf

'''
DESPUES DE IMPORTAR LA LIBRERIA PODEMOS USAR SUS HERRAMIENTAS.

EL MODULO Ticker NOS PERMITE EL ACCESO A LA COMPAÑIA DE BASE DE DATOS EN SU SIMBOLO DE COTIZACION DEL MERCADO.

POR EJEMPLO TOMEMOS DATOS DE TESLA
'''

data = yf.Ticker("TSLA")

'''
AHORA PODEMOS ACCEDER A LA INFORMACION DE LA COMPAÑIA BAJO LOS CAMPOS CORRESPONDIENTES

POR EJEMPLO, PARA OBTENER DATOS GENERALES
'''

print(data.info)

'''
OBTENGAMOS LOS MARGENES DE BENEFICIO Y RoE:
'''

print(data.info['profitMargins'])
print(data.info['returnOnEquity'])

'''
Además de los campos de información, el objeto de datos proporciona los siguientes campos:
'''

# print(data.actions)

#Dividendos:
# print(data.dividends)

# #Divisiones:
# print(data.splits)

#Hoja de balance:
print(data.balance_sheet)

#Flujo de efectivo:
print(data.cashflow)

#Gananacias:
print(data.earnings)

'''
TAMBIEN PODEMOS GRAFICAR FACILMENTE LOS DATOS.

POR EJEMPLO CREEMOS UN GRAFICO DE BARRAS PARA LOS INGRESOS:
'''

import matplotlib.pyplot as plt

x = data.earnings

x.plot(kind = 'bar')

plt.savefig('ingresos.png')

