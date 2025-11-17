# -------------------------------
# bank_transactions.py
# Demonstrates functions, file handling, and exceptions
# -------------------------------
import datetime

def log_transaction(name, action, amount, balance):
    """Log every transaction in a text file."""
    # Use UTF-8 so the ₹ symbol is supported on all systems
    with open("transactions.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {name} - {action} ₹{amount} - Balance: ₹{balance}\n")

def deposit(name, balance, amount):
    balance += amount
    print(f"{name} deposited ₹{amount}. New balance: ₹{balance}")
    log_transaction(name, "DEPOSIT", amount, balance)
    return balance

def withdraw(name, balance, amount):
    if amount > balance:
        print(f"{name} cannot withdraw ₹{amount}. Insufficient funds.")
    else:
        balance -= amount
        print(f"{name} withdrew ₹{amount}. New balance: ₹{balance}")
        log_transaction(name, "WITHDRAW", amount, balance)
    return balance


# Demo
if __name__ == "__main__":
    name = "John"
    balance = 5000

    balance = deposit(name, balance, 2000)
    balance = withdraw(name, balance, 3000)
    balance = withdraw(name, balance, 5000)

    print("\nAll transactions saved in transactions.txt")
