# Take the BankAccount class and make account objects truthy when the balance attribute is non-zero and falsey when the balance is zero.
#
# You can use this class:
#
# class BankAccount:
#
#     def __init__(self, balance=0):
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
# Hint:
#   Use __bool__ method

class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __bool__(self):
        return self.balance > 0