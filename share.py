class Share:

    def __init__(self, symbol):
        self._symbol = symbol
        self._price = 0

    def __repr__(self):
        return """
            Symbol: {},
            Price: {},
        """.format(self._symbol_name, self._price)
