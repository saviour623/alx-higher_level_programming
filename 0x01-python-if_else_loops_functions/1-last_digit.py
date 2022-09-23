#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number) % 10
if number < 0:
    x = x * -1
if x == 0:
    print(f"Last digit of {number} is {x:d} and is 0")
elif x < 6 and x != 0:
    print(f"Last digit of {number} is {x:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {x:d} and is greater than 5")
