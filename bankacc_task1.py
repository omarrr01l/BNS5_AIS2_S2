class BankAccount:
    def __init__(self, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount(100)
account.deposit(50)       
account.withdraw(30)    
account.check_balance()