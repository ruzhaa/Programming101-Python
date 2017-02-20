class BankAccount():
    def __init__(self, name, balance, currency):
        self.__name = name
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError
        self.__currency = currency
        self.messages_for_history = []
        self.messages_for_history.append('Account was created')

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.messages_for_history.append('Deposited {}{}'.format(amount, self.__currency))
        else:
            raise ValueError

    def balance(self):
        self.messages_for_history.append('Balance check -> {}{}'.format(self.__balance, self.__currency))
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.balance():
            self.__balance -= amount
            self.messages_for_history.append('{}{} was withdrawed'.format(amount, self.__currency))
            return True
        else:
            self.messages_for_history.append('Withdraw for {}{} failed'.format(amount, self.__currency))
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}"\
            .format(self.__name, self.__balance, self.__currency)

    def __int__(self):
        self.messages_for_history.append('__int__ check -> {}{}'.format(self.__balance, self.__currency))
        return int(self.__balance)

# account == other
    def transfer_to(self, account, amount):
        if self.__currency == account.__currency:
            account.__balance += amount
            self.__balance -= amount
            self.messages_for_history.append('Transfer to {} for {}{}'.format(account.__name, amount, account.__currency))
            return True
        else:
            return False

    def history(self):
        return self.messages_for_history
