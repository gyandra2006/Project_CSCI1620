from operator import truediv
from sys import flags
from xmlrpc.client import boolean

class Account:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        if balance > 0:
            self.__account_balance = balance
        else:
            self.__account_balance = 0
        self.set_balance(self.__account_balance)

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if (amount > 0) and (self.__account_balance >= amount):
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_account_number(self):
        return self.__account_number

    def set_balance(self, value):
        if value > 0:
            self.__account_balance = value
        else:
            self.__account_balance = 0

    def set_account_number(self, value):
        self.__account_number = value


class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name):
        super().__init__(name, SavingAccount.MINIMUM)
        self.__deposit_count = 0

    def apply_interest(self):
        if self.__deposit_count % 5 == 0:
            total = self.get_balance() + (0.02 * self.get_balance())
            self.set_balance(total)

    def deposit(self, amount):
        if amount > 0:
            super().deposit(amount)
            self.__deposit_count += 1
            self.apply_interest()
            return True
        else:
            return False

    def withdraw(self, amount):
        if (amount > 0) and ((self.get_balance() - 100) >= amount):         
            x = self.get_balance() - amount
            self.set_balance(x)
            return True
        else:
            return False

    def set_balance(self, value):
        if value < SavingAccount.MINIMUM:
            super().set_balance(SavingAccount.MINIMUM)
        else:
            super().set_balance(value)


    def __str__(self):
        return f'SAVING ACCOUNT = {super().__str__()}'