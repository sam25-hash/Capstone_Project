# -------------------------------
# bank_oop.py
# Demonstrates OOP in Python
# -------------------------------

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew ₹{amount}. Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient Balance")


class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} added. New Balance: ₹{self.balance:.2f}")


# Demo execution
if __name__ == "__main__":
    acc = SavingsAccount("Asha", 5000)
    acc.deposit(1000)
    acc.add_interest()
    acc.withdraw(2000)