# import yfinance as yf
from urllib import response
import time
import requests
headers = {"X-Finnhub-Token": "ccsbj7iad3ifi21dalvgccsbj7iad3ifi21dam00"}


class StockApi:

    def get_share_price(self, symbol):
        api_url = 'https://finnhub.io/api/v1/quote?symbol={}'.format(symbol)
        response = requests.get(api_url, headers=headers)
        return response.json()['c']

    def get_share_price_by_date(self, symbol, epoch_from, epoch_to):
        api_url = f'https://finnhub.io/api/v1/stock/candle?symbol={symbol}&resolution=D&from={epoch_from}&to={epoch_to}'
        response = requests.get(api_url, headers=headers)
        print(response.json()['c'][0])
