from datetime import datetime
from enum import Enum


class TransactionTypes(Enum):
    DEPOSIT = 0
    WITHDRAW = 1
    BUY = 2
    SELL = 3


class Transaction:

    transaction_types = {
        'deposit': 'deposit',
        'withdraw': 'withdraw',
        'buy': 'buy',
        'sell': 'sell'
    }

    def __init__(self, transaction_type, share, string_date):
        self._type = transaction_type
        self._share = share
        self._date = self._string_date_to_datetime(string_date)

    def _string_date_to_datetime(self, string_date):
        datetime_object = datetime.strptime(string_date, '%Y-%m-%d')
        return datetime_object
