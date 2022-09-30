#!/usr/bin/python3
import sys
import hidden_4

if __name__ == '__main__':
    def main():
        for i in div(hidden_4):
            if i[:2] == '__':
                break
            print(i)
    main()
