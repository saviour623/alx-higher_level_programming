#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
x = int(number[-1])
if number[0] == '-':
    x = x * -1
if x > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")
elif int(number[-1]) == 0:
    print(f"Last digit of {number} is {(x)} and is 0")
elif int(number[-1]) < 6 and int(number[-1]) != 0:
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
