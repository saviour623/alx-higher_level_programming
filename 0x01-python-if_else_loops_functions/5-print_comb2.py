#!/usr/bin/python3
for i in range(0, 99):
    if i <= 9:
        print(0, end="")
    print(i, end="")
    if i != 98:
        print(", ", end="")
print()
