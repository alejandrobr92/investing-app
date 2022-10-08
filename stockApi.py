# import yfinance as yf
import requests
headers = {"X-Finnhub-Token": "ccsbj7iad3ifi21dalvgccsbj7iad3ifi21dam00"}


class StockApi:

    def get_share_price(self, symbol):
        api_url = 'https://finnhub.io/api/v1/quote?symbol={}'.format(symbol)
        response = requests.get(api_url, headers=headers)
        return response.json()['c']
