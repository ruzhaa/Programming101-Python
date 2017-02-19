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


class BatchBill:
    def __init__(self, list_of_bills):
        self._bills = list_of_bills

    def __len__(self):
        return len(self._bills)

    def __getitem__(self, index):
        return self._bills[index]

    def total(self):
        return sum([bill.total() for bill in self._bills])


class CashDesk:

    def __init__(self):
        self.total_amount = []

    def take_money(self, temp):
        self.total_amount.append(temp)

    def total(self):
        return sum([bill.total() for bill in self.total_amount])

    def inspect(self):
        text = []
        text.append("We have a total of {}$ in the desk".format(self.total()))
        bills = []

        if self.total() > 0:
            text.append("We have the following count of bills, sorted in ascending order:")

            for bill in self.total_amount:
                if isinstance(bill, BatchBill):
                    for one_bill in bill:
                        bills.append(one_bill.total())
                else:
                    bills.append(bill.total())
            for bill in sorted(set(bills)):
                text.append("{}$ bills - {}".format(bill, bills.count(bill)))
            return "\n".join(text)


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

desk.total()
print(desk.inspect())
