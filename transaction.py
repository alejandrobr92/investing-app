class Transaction:

    transaction_types = {
        'deposit': 'deposit',
        'withdraw': 'withdraw',
        'buy': 'buy',
        'sell': 'sell'
    }

    def __init__(self, type, share, date):
        self._type = type
        self._share = share
        self._date = date
