# dice simulator
import random
print("Welcome to the dice simulator")
print("Get ready to roll")

number_rolls = int(input("How many rolls do you want?" ))

two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

for iteration in range(number_rolls):
    roll = random.randint(1,6) + random.randint(1,6)

    if roll == 2:
        two += 1
    elif roll == 3:
        three += 1
    elif roll == 4:
        four += 1
    elif roll == 5:
        five += 1
    elif roll == 6:
        six += 1
    elif roll == 7:
        seven += 1
    elif roll == 8:
        eight += 1
    elif roll == 9:
        nine += 1
    elif roll == 10:
        ten += 1
    elif roll == 11:
        eleven += 1
    elif roll == 12:
        twelve += 1

print('Results'.center(20))
print("-" * 20)
print(f"{'Twos:':<10}{two * '|'}")
print(f"Threes:   {three * '|'}")
print(f"Fours:    {four * '|'}")
print(f"Fives:    {five * '|'}")
print(f"Six:      {six * '|'}")
print(f"Seven:    {seven * '|'}")
print(f"Eight:    {eight * '|'}")
print(f"Nines:    {nine * '|'}")
print(f"Tens:     {ten * '|'}")
print(f"Elevens:  {eleven * '|'}")
print(f"Twelves:  {twelve * '|'}")







