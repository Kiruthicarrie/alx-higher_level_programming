#!/usr/bin/python3
def uppercase(str):
    upper = 0
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            upper = 32
        else:
            upper = 0
        print("{:c}".format(ord(x)-upper), end="")

    print()
