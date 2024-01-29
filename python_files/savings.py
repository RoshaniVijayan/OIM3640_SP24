# savings calculator in-class 3

print("Welcome to the savings calcuator")
print("Enter your initial deposit and see the ending balances")

deposit = float(input("Enter deposit amount: "))
RATE = .015
print(f"{'Year':15}{'Balance':>9}")
print("_" * 24)

for year in range(1,6):
    deposit += (1 + RATE)
    # deposit = deposit * (1 + RATE)
    print(f"{year:<15}$ {deposit:<14,.2f}")