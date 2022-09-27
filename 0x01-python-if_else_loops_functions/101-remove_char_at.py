#!/usr/bin/python3
def remove_char_at(str, n):
    strn = ""
    for i in str:
        if n == str.index(i):
            continue
        strn += i
    print(strn)
