class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def print_balance(self):
        return self.balance


account = BankAccount()
account.deposit(100)
account.deposit(100)
account.deposit(500)
print(account.print_balance())
account.withdraw(900)
print(account.print_balance())
