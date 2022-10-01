class Transaction:

    transaction_types = {
        'deposit': 'deposit',
        'withdraw': 'withdraw',
        'buy': 'buy',
        'sell': 'sell'
    }

    def __init__(self, type, share, date):
        self.__type = type
        self.__share = share
        self.__date = date
