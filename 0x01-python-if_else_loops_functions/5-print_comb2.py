#!/usr/bin/python3
for i in range(0, 99):
    if i <= 9:
        print("{:d}".format(0), end="")
    print("{:d}".format(i), end="")
    if i != 98:
        print(", ", end="")
print()
