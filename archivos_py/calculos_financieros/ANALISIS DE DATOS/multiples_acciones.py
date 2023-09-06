'''
TOMEMOS TRES DIFERENTES TICKERS (EMPRESAS) Y USEMOS LA FUNCION pct_change() PARA CALCULAR EL RENDIMIENTO DIARIO:
'''
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as scipy

#El siguiente codigo no funciono con la funcion download:

data = yf.download("TSLA", start='2021-01-01')

x = data['Close'].pct_change()

print(x.describe())


