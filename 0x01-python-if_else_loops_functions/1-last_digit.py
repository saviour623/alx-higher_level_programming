#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = "{}".format(number)
x = int(number[-1])
if number[0] == '-':
    x = x * -1
if x == 0:
    text = "and is 0"
elif x < 6 and x != 0:
    text = "and is less than 6 and not 0"
else:
    text = "and is greater than 5"
print(f"Last digit of {number:s} is {x:d} {text:s}")
