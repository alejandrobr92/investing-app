class Portfolio:

    transaction_types = {
        'deposit': 'deposit',
        'withdraw': 'withdraw',
        'buy': 'buy',
        'sell': 'sell'
    }

    def __init__(self):
        self._current_value = 0
        self._transactions = []
        self._shares = []

    def __is_transaction_valid(self, transaction):
        # if transaction_type == self.transaction_types['withdraw'] and self.__current_value < transaction.:
        # if transaction.type == self.transaction_types['deposit']:
        pass

    def add_transaction(self, transaction):
        if self._is_transaction_valid(transaction):
            self._transactions.append(transaction)
        else:
            print('Transaction is not valid')

    def get_portfolio_value(date):

        pass
