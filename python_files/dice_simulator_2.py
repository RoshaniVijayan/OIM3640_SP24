# dice simulator
import random

print("Welcome to the dice simulator")
print("Get ready to roll")

number_rolls = int(input("How many rolls do you want?" ))
counts = [0 for x in range(11)]
roll_values = list(range(2,13))
for count in range(number_rolls):
    roll = random.randint(1,6) + random.randint(1,6)

    if roll == 2:
        counts[0] +=1
    elif roll == 3:
        counts[1] += 1
    elif roll == 4:
        counts[2] += 1
    elif roll == 5:
        counts[3] += 1
    elif roll == 6:
        counts[4] += 1
    elif roll == 7:
        counts[5] += 1
    elif roll == 8:
        counts[6] += 1
    elif roll == 9:
        counts[7] += 1
    elif roll == 10:
        counts[8] += 1
    elif roll == 11:
        counts[9] += 1
    elif roll == 12:
        counts[10] += 1

print("Results".center(20))
for value in range(11):
    print(f"{roll_values[value]:10}:{'|' * counts[value]}")


