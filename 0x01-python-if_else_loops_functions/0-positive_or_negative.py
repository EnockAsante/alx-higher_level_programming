#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number != abs(number):
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is positive")
