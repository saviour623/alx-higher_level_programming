#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == '__main__':

    warning = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    a_len = len(argv)
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if a_len - 1 != 3:
        print("{}".format(warning))
        exit 1
    if op == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == "-":
        print("{:d} - {:d} = {:d}".format(a,  b, sub(a, b)))
    elif op == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif op == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit 1
