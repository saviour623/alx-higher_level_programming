#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print("{a} + {b} = {:d}".format(a=a, b=b, add(a, b)))
print("{a} - {b} = {:d}".format(a=a, b=b, sub(a, b)))
print("{a} * {b} = {:d}".format(a=a, b=b, mul(a, b)))
print("{a} / {b} = {:d}".format(a=a, b=b, div(a, b)))
