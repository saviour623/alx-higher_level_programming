#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
x = abs(int(number[-1]))
if number[0] == '-':
    x = x * -1
if int(number[-1]) == 0:
    text = "and is 0"
elif x < 6 and x:
    text = "and is less than 6 and not 0"
else:
    text = "and is greater than 5"
print(f"Last digit of {number} is {x:d} {text}")
