class Bill:
    def __init__(self, amount):
        self._amount = amount

    def __str__(self):
        return "A {}$ bill".format(self._amount)

    def __repr__(self):
        return str(self)

    def __int__(self):
        return int(self._amount)

    def __eq__(self, other):
        return self._amount == other._amount

    def __hash__(self):
        return hash(self._amount)

    def total(self):
        return self._amount
