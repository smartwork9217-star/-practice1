"""Create InsufficientFundsError(Exception)
BankAccount(owner, balance=0) with deposit and withdraw
withdraw raises the error if the amount is more than the balance
Start with 1000, deposit 500, withdraw 300, print balance
Try to withdraw 5000 and catch the error"""

class InsufficientFundsError(Exception):
    pass

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        self.balance -= amount

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)
print(account.balance)

try:
    account.withdraw(5000)
except InsufficientFundsError as e:
    print(f"Error: {e}")