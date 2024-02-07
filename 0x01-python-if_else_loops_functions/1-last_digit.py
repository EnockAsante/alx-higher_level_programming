#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = 0
numb_dub = abs(number)
if numb_dub > 0:
    rem = int(numb_dub % 10)

print(f"last digit of {number} is {rem} ", end="")
if rem > 5:
    print("and is greater than 5")
elif rem == 0:
    print("and is 0")
elif rem < 6:
    print("and is less than 6 and not 0")
