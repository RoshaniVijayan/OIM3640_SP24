# random numbers
import matplotlib.pyplot as plt
import os
import random

file = open('data/numbers.txt', 'w')

for integer in range(1,501):
    random_int = random.randint(1, integer)
    file.write(f"{random_int}\n")
    
file.close()

file = open('data/numbers.txt', 'r')
data = []
for value in file.readlines():
    data.append(int(value.strip()))
print(data)

plt.plot(data)
plt.show()




    