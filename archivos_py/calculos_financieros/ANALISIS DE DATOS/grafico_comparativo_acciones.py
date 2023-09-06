import yfinance as yf
import matplotlib.pyplot as plt

# Definir los símbolos de las acciones a comparar
symbols = ["AAPL", "MSFT", "TSLA","META"]

# Descargar los datos históricos de las acciones
data = yf.download(symbols, start="2021-06-01", end="2023-05-15")

# Seleccionar el precio de cierre ajustado
adj_close = data["Adj Close"]

# Graficar los precios de las acciones
adj_close.plot(figsize=(10,6))
plt.title("Comparación de precios de acciones")
plt.xlabel("Fecha")
plt.ylabel("Precio de cierre ajustado")
plt.show()

