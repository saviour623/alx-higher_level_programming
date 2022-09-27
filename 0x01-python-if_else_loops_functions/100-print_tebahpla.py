#!/usr/bin/python3
i = 122
while i >= 97:
    print("{:s}".format(chr(i)), end="");
    if (i - 1) >= 97:
        i = i - 1
        print("{:s}".format(chr(i - 32)), end="")

    i = i - 1
