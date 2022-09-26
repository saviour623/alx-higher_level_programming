#!/usr/bin/python3
41;320;0cdef uppercase(str):
    str1 = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            str1 += chr(ord(i) - 32)
        else:
            str1 += i
    print("{:s}".format(str1))
