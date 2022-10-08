from datetime import datetime
from enum import Enum


class TransactionTypes(Enum):
    BUY = 2
    SELL = 3


class Transaction:

    def __init__(self, type: TransactionTypes, share, quantity):
        self._type = type
        self._share = share
        self._quantity = quantity
        #self._date = self._string_date_to_datetime(string_date)

    def __repr__(self):
        return """
            Type: {}
            Share: {}
            Quantity: {}
            """.format(self._type, self._share, self._quantity)

    def _string_date_to_datetime(self, string_date):
        datetime_object = datetime.strptime(string_date, '%Y-%m-%d')
        return datetime_object
