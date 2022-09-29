#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    def main(argv):
        a_len = len(argv) - 1
        if a_len  == 1:
            print("{:d} argument".format(a_len))
        else:
             print("{:d} arguments".format(a_len))

        for i in range(1, len(argv)):
            s = ":"
            print("{:d}".format(i), end="")
            if argv[i]:
                print("{:s} {:s}".format(s, argv[i]))
            else:
                s = "."
                print("{:s}".format(s))
    main(argv)
