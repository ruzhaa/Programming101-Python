class BankAccount():
    def __init__(self, name, balance, currency):
        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.list_history = []
        self.list_history.append("Account was created")

    def deposit(self, amount):
        self.__balance += amount
        self.list_history.append("Deposited {}{}".format(amount, self.__currency))
        return self.__balance

    def balance(self):
        self.list_history.append("Balance check -> {}{}".format(self.__balance, self.__currency))
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.balance():
            self.__balance -= amount
            return True
        else:
            self.list_history.append("{}{} was withdrawed".format(amount, self.__currency))
            return False

    def __str__(self):
        text = "Bank account for {} with balance of {}{}".\
              format(self.__name, self.balance(), self.__currency)
        self.list_history.append(text)
        return text

    def __int__(self):
        self.list_history.append("__int__ check -> {}{}".format(self.__balance, self.__currency))
        return int(self.balance())

    def transfer_to(self, account, amount):
        if account.__currency == self.__currency:
            account.__balance += amount
            self.__balance -= amount
            self.list_history.append("{}{} was withdrawed".format(amount, self.__currency))
            return True
        else:
            self.list_history.append("Withdraw for {}{} failed.".format(amount, self.__currency))
            return False

    def history(self):
        return self.list_history
