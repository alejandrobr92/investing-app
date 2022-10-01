
import unittest

from share import Share


class TestShare(unittest.TestCase):

    def test_get_value(self):

        share = Share('AAPL', 1)
        print(share._price)
