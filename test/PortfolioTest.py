import unittest

from portfolio import Portfolio
from transaction import Transaction
from share import Share


class TestPortfolio(unittest.TestCase):

    def test_add_deposit(self):
        portfolio = Portfolio()
        portfolio.add_deposit(1000)
        self.assertEqual(1000, portfolio.get_portfolio_value())

    def xxx_test_add_transaction_valid(self):
        portfolio = Portfolio()
        transaction1 = Transaction('deposit', None, '2022-10-01')
        portfolio.add_transaction(transaction1)
        portfolio.get_portfolio_value()
        aapl_share = Share('AAPL', 2)
        transaction2 = Transaction('buy', aapl_share, '2022-10-02')
        portfolio.add_transaction(transaction2)
