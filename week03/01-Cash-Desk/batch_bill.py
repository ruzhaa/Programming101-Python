from bill import Bill


class BatchBill:
    def __init__(self, list_of_bills):
        self._bills = list_of_bills

    def __len__(self):
        return len(self._bills)

    def __getitem__(self, index):
        return self._bills[index]

    def total(self):
        bill = Bill(self)
        return sum([bill.total() for bill in self._bills])
