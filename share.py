
import yfinance as yf

hard_coded_values = {
    'AAPL': 300,
    'GOOGL': 500,
    'AMZN': 200,
}


class Share:

    def __init__(self, symbol_name, quantity):
        self._symbol_name = symbol_name
        self._quantity = quantity
        #self._price = hard_coded_values[symbol_name] #get value from internet
        stock_info = yf.Ticker(symbol_name).info
        self._price = stock_info['regularMarketPrice']

