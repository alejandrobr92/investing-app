from transaction import TransactionTypes
from functools import reduce


class Portfolio:

    def __init__(self):
        self._current_value = 0.0  # shares + cash
        self._transactions = []
        self._shares = []
        self._current_cash = 0.0
        self._current_shares_value = 0.0

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
        elif transaction._type == TransactionTypes.SELL and self._get_total_shares_available_by_symbol >= transaction._quantity:
            return True
        else:
            return False

    def _make_transaction(self, transaction):
        if transaction._type == TransactionTypes.BUY:
            self._buy_shares(transaction)

    def _buy_shares(self, transaction):
        total_transaction = transaction._share._price * transaction._quantity
        self._current_cash -= total_transaction
        self._update_current_value()

    def get_portfolio_value(self, date=None):
        return self._current_value

    def _update_current_value(self):
        self._current_value = self._current_cash + self._current_shares_value

    def _get_total_shares_available_by_symbol(self, symbol):
        # filtered_transactions = filter(self._filter_transactions_by_symbol, self._transactions)
        print(len(self._transactions))
        filtered_transactions = [
            transaction for transaction in self._transactions if transaction._share._name_symbol == symbol]
        print(len(filtered_transactions))
        total_shares_available = reduce(
            lambda a, b: a._quantity + b.quantity, filtered_transactions)
        print(total_shares_available)
        return total_shares_available

    # def _filter_transactions_by_symbol(transaction, symbol):
    #    return transaction._share._name_symbol == symbol
