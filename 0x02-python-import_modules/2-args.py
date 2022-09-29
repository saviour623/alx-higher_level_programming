#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
        p = "."
        s = ":"
        sp = ": "
        ar1 = "argument"
        ar2 = "arguments"
        a_len = len(argv) - 1

        if a_len  == 1:
            print("{:d} {:s}{:s}".format(a_len, ar1, s))
        elif a_len == 0:
            print("{:d} {:s}{:s}".format(a_len, ar2, p))
        else:
            print("{:d} {:s}{:s}".format(a_len, ar2, s))

        for i in range(1, len(argv)):
            print("{:d}{:s}{:s}".format(i, sp, argv[i]))
