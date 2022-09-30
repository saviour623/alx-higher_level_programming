#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import hidden_4
    def main():
        for i in div(hidden_4):
            if i[:2] != '__':
                print(i)
    main()
