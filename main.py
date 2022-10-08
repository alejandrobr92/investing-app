from stockApi import StockApi
from portfolio import Portfolio
from share import Share
from transaction import Transaction, TransactionTypes

api = StockApi()
portfolio = Portfolio()

portfolio.make_deposit(1000)
print(portfolio._current_cash)
print(portfolio._current_value)

apple_share = Share('AAPL')
apple_share._price = api.get_share_price(apple_share._symbol)
twitter_share = Share('TWTR')
twitter_share._price = api.get_share_price(twitter_share._symbol)
print(apple_share._price)
print(twitter_share._price)

first_transaction = Transaction(TransactionTypes.BUY, apple_share, quantity=2)
portfolio.add_transaction(first_transaction)

third_transaction = Transaction(
    TransactionTypes.BUY, twitter_share, quantity=1)
portfolio.add_transaction(third_transaction)

print(portfolio._shares)
print(portfolio._current_cash)
print(portfolio._current_value)

second_transaction = Transaction(
    TransactionTypes.SELL, apple_share, quantity=1)
portfolio.add_transaction(second_transaction)

print(portfolio._shares)
print(portfolio._current_cash)
print(portfolio._current_value)

print(api.get_share_price_by_date('AAPL', 1662737611, 1662824011))
