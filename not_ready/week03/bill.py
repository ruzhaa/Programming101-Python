class Bill:
    def __init__(self, amount):
        if amount < 0:
            raise ValueError
        try:
            self._amount = amount
        except:
            raise TypeError

    def __str__(self):
        return "A {}$ bill".format(self._amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self._amount)

    def __eq__(self, other):
        return self._amount == other._amount

    def __hash__(self):
        return hash(self._amount)

    def total(self):
        return self._amount
