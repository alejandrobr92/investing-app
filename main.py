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
apple_share._price = api.get_share_price(apple_share._symbol_name)
print(apple_share._price)

first_transaction = Transaction(TransactionTypes.BUY, apple_share, quantity=2)

portfolio.add_transaction(first_transaction)

print(portfolio._current_cash)
print(portfolio._current_value)

second_transaction = Transaction(
    TransactionTypes.SELL, apple_share, quantity=1)

print(portfolio._current_cash)
print(portfolio._current_value)
