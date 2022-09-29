#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    def main(argv):
        sum1 = 0
        for i in range(1, len(argv)):
            sum1 += int(argv[i])
        print("{:d}".format(sum1))

    main(argv)
