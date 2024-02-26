# assign 2 starter

import numpy_financial as npf


choice = input("[S]ample report or [C]ustom report? ").lower()
while choice not in 'sc':
    print("Incorrect choice. Enter S or C")
    choice = input("[S]ample report or [C]ustom report? ").lower()

if choice == 's':
    rate = 5.875
    term = 30
    pv = 360000

else:
    rate = float(input("Enter interest rate: "))
    term = int(input("Enter loan term in years ( 10 - 40): "))
    pv = float(input("Enter amount borrowed: "))

remaining = pv
int_paid = 0
prin_paid = 0
pmt_paid = 0
half_paid = False


print(f"{'Month':<10}{'Payment':>12}{'Interest':>12}{'Principal':>12}{'Remaining':>16}")
print("-" * 62)
for month in range(1, term * 12 + 1):
    pmt = npf.pmt(rate /1200, term * 12, -pv)
    interest = npf.ipmt(rate /1200, month, term * 12, -pv)
    principal = npf.ppmt(rate /1200, month, term * 12, -pv)
    remaining -= principal
    pmt_paid += pmt
    int_paid += interest
    prin_paid += principal

    if prin_paid >= pv / 2 and half_paid == False:
        half_month = month
        half_paid = True

    print(f"{month:<10}{pmt:>12,.2f}{interest:>12,.2f}{principal:>12,.2f}{remaining:>16,.2f}")

print("-" * 62)
print(f"{pmt_paid:<12,.2f}{int_paid:>12,.2f}{prin_paid:>12,.2f}")
print(f"{half_month}")