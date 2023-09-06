'''
TAMBIEN PODEMOS ACCEDER A DATOS SOBRE INVERSORES DE LA EMPRESA

OBTENGAMOS LA LISTA DE LOS PRINCIPALES TITULARES DE TESLA.
'''

import yfinance as yf

data = yf.Ticker('TSLA')

print(data.major_holders)

#TAMBIEN PODEMOS ACCEDER A LA LISTA DE INSTITUCIONES TITULARES:

print(data.institutional_holders)

'''
OBTEBER LOS INVERSORES INSTUITUCIONALES QUE TENGAN MAS DE 10M DE ACIONES.
'''

x = data.institutional_holders

print(x[x['Shares'] > 10000000])

'''
EL CAMPO recommendations PROPORCIONA RECOMENDACIONES HISTORICAS DE LOS BANCOS DE INVERSION.
'''

y = data.recommendations
y = y[y.index > '2021-06-01']
print(y)

