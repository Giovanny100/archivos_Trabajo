#SE PUEDE OBTENER EL VALOR MAXIMO DE INVERSION:
import yfinance as yf

data = yf.Ticker('SPY MSFT AAPL')

print(data['Close'].max())