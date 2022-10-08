from transaction import TransactionTypes
from functools import reduce
from stockApi import StockApi


class Portfolio:

    def __init__(self):
        self._current_value = 0.0  # shares + cash
        self._transactions = []
        self._shares = {}
        self._current_cash = 0.0
        self._current_shares_value = 0.0
        self._api = StockApi()

    def __repr__(self):
        return """
            Current value: {},
            Transactions: {}
            """.format(self._current_value, self._transactions)

    def make_deposit(self, amount):
        self._current_cash += amount
        self._update_current_value()

    def make_withdraw(self, amount):
        self._current_cash -= amount
        self._update_current_value()

    def add_transaction(self, transaction):
        if self._is_transaction_valid(transaction):
            self._make_transaction(transaction)
            self._transactions.append(transaction)
        else:
            print('Transaction is not valid')

    def _is_transaction_valid(self, transaction):
        if transaction._type == TransactionTypes.BUY and self._current_cash >= (transaction._share._price * transaction._quantity):
            return True
        elif transaction._type == TransactionTypes.SELL and transaction._share._symbol in self._shares and self._shares[transaction._share._symbol]['quantity'] >= transaction._quantity:
            return True
        else:
            return False

    def _make_transaction(self, transaction):
        if transaction._type == TransactionTypes.BUY:
            self._buy_shares(transaction)
        else:
            self._sell_shares(transaction)
        self._update_current_shares_value()
        self._update_current_value()

    def _buy_shares(self, transaction):
        total_transaction = transaction._share._price * transaction._quantity
        self._current_cash -= total_transaction
        if transaction._share._symbol in self._shares:
            print(type(self._shares[transaction._share._symbol]))
            self._shares[transaction._share._symbol]['quantity'] += transaction._quantity
        else:
            self._shares[transaction._share._symbol] = {'quantity': 0}
            self._shares[transaction._share._symbol]['quantity'] = transaction._quantity

    def _sell_shares(self, transaction):
        total_transaction = transaction._share._price * transaction._quantity
        self._current_cash += total_transaction
        self._shares[transaction._share._symbol]['quantity'] -= transaction._quantity

    def get_portfolio_value(self, date=None):
        return self._current_value

    def _update_current_shares_value(self):
        total_value = 0
        for share in self._shares:
            price = self._api.get_share_price(
                share) * self._shares[share]['quantity']
            total_value += price
        self._current_shares_value = total_value

    def _update_current_value(self):
        self._current_value = self._current_cash + self._current_shares_value
