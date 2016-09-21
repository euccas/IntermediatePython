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
#
# >>> account1 = BankAccount(balance=100)
# >>> account2 = BankAccount(balance=200)
# >>> account1 == account2
# False
# >>> account1 < account2
# True
# >>> account1 >= account2
# False

class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __bool__(self):
        return self.balance > 0

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance
