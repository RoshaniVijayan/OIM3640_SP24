# reaction time tester

import random
import time

print("Welcome to the reaction time tester")
print("when a prompt appears hit the enter key!")
print("You will have five tries!")
print("Get ready!")

times = []
time.sleep(1)
for attempt in range(5):
    time.sleep(random.uniform(0, 5))
    start = time.time()
    input("Quick! Hit enter")
    reaction = time.time() - start
    times.append(reaction)
    print("Wow that was quick!")
    print(f"It took you {reaction:.3f} seconds to hit enter")
print("Summary Report".center(30, "-"))
print(f"Your fastest time was: {min(times):.3f}")
print(f"Your slowest time was: {max(times):.3f}")
print(f"Your average time was: {sum(times) / len(times):.3f}")