import email
# from typing_extensions import Self
from unicodedata import name


class BankAccount:

    accounts = []

    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $1 fee")
            self.balance -= 1
        return self


    def display_account_info(self):
        print(f"balance:{self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

checking = BankAccount(.03, 10000)
savings = BankAccount(.01, 20000)

checking.deposit(1200).withdraw(400).yield_interest().display_account_info()
savings.deposit(500).yield_interest().display_account_info()

BankAccount.print_all_accounts()

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.email = email
#         self.account = {
#             "checking" : BankAccount(0.2,0),
#             "savings" : BankAccount(0.4, 12000)
#         }

#     def make_deposit(self, amount):
#         self.account.deposit += amount
#         print(self.account.balance)
#         return self

#     def make_withdraw(self, amount):
#         if (BankAccount.balance - amount) >= 300:
#             BankAccount.balance -= amount
#         return self

#     def display_user_balance(self):
#         print(f"User: {self.name}, balance: {self.account['checking'].display_account_info()}")
#         print(f"User: {self.name}, savings balance:{self.account['savings'].display_account_info()}")

# Chidi = User("Chidi")

# Chidi.account['savings'].deposit(9000)
# Chidi.account['checking'].deposit(11000)
# Chidi.display_user_balance()