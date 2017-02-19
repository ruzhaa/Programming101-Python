import unittest
from bank_account import BankAccount


class Test(unittest.TestCase):

    def setUp(self):
        self.rado = BankAccount("Rado", 1000, "$")

    def test_bank_account_deposit(self):
        self.assertEqual(self.rado.deposit(1000), 2000)

    def test_balance(self):
        self.assertEqual(self.rado.balance(), 1000)

    def test_withdraw(self):
        self.assertEqual(self.rado.withdraw(300), True)

    def test_str(self):
        self.assertEqual(str(self.rado), "Bank account for Rado with balance of 1000$")

    def test_int(self):
        self.assertEqual(int(self.rado), 1000)

    def test_transfer_to_account(self):
        self.ivo = BankAccount("Ivo", 3000, "$")
        self.assertEqual(self.rado.transfer_to(self.ivo, 20), True)


if __name__ == '__main__':
    unittest.main()
