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
