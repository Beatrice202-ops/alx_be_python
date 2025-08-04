class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"

# Demonstrate deposit and withdrawal, then print balance
account = BankAccount()
account.deposit(300)
account.withdraw(50)
print(account.display_balance())



