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


class BillBatch:
    def __init__(self, list_of_bills):
        self.list_of_bills = list_of_bills

    def __len__(self):
        return len(self.list_of_bills)

    def total(self):
        return sum([bill.total() for bill in self.list_of_bills])

    def __getitem__(self, index):
        return self.list_of_bills[index]


class CashDesk:
    def __init__(self):
        self.total_amount = []

# money can be either Bill or BillBatch
    def take_money(self, money):
        self.total_amount.append(money)

    def total(self):
        return sum([bill.total() for bill in self.total_amount])

    def inspect(self):
        list_of_strings = []
        list_of_strings.append("We have a total of {}$ in the desk"\
                       .format(self.total()))
        bills = []
        if self.total() > 0:
            list_of_strings.append("We have the following count of bills,\
                            sorted in ascending order:")
            for bill in self.total_amount:
                if isinstance(bill, BillBatch):
                    for one_bill in bill:
                        bills.append(one_bill.total())
                else:
                    bills.append(bill.total())

            for bill in sorted(bills):
                list_of_strings.append("{}$ bills - {}"\
                               .format(bill, bills.count(bill)))
            return "\n".join(list_of_strings)
