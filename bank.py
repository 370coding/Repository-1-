# from typing_extensions import Self


class Bankaccount:

    accounts =  []

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $2 fee")
            self.balance -= 1
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate)
        return self

account_1 = Bankaccount(0.3,5000)
account_2 = Bankaccount(0.4,2000)

account_1.deposit(100000).deposit(1000).deposit(5000).withdraw(5000).yield_interest().display_account_info()
account_2.deposit(5000).deposit(5000).withdraw(1000).withdraw(1000).withdraw(500).withdraw(100).yield_interest().display_account_info()

