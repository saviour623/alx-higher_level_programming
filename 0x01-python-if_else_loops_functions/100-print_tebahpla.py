#!/usr/bin/python3
i = 122
while i >= 97:
    print("{:s}{:s}".format(chr(i), chr((i - 1) - 32)), end="")
    i = i - 2
