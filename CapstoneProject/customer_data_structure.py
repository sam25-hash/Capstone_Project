# -------------------------------
# customer_data_structures.py
# Demonstrates Python data Structures
# -------------------------------

customers = [
    {"id": 1, "name": "John", "balance": 5000},
    {"id": 2, "name": "Asha", "balance": 10000},
    {"id": 3, "name": "Raj", "balance": 7500},
]

# List of names
names = [c["name"] for c in customers]
print("Customer Names:", names)

# Set of unique balances
balances = {c["balance"] for c in customers}
print("Unique Balances:", balances)

# Dictionary: name -> balance
balance_map = {c["name"]: c["balance"] for c in customers}
print("Name to Balance Map:", balance_map)

# Find richest customer
richest = max(customers, key=lambda x: x["balance"])
print(f"Richest Customer: {richest['name']} with ₹{richest['balance']}")

# Save customer data to CSV file
import csv

with open("customers.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "balance"])
    writer.writeheader()
    writer.writerows(customers)

print("Customer data saved to customers.csv successfully.")