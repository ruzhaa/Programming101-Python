from bill import Bill
from batch_bill import BatchBill


class CashDesk:

    def __init__(self):
        self.total_amount = []

    def take_money(self, temp):
        self.total_amount.append(temp)

    def total(self):
        return sum([bill.total() for bill in self.total_amount])
