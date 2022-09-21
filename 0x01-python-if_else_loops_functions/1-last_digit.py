#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = (abs(number) % 10)
if number < 0:
    lastDigit = lastDigit * -1

msg = "Last digit of {0} is {1} and is"
if lastDigit > 5:
    print(msg.format(number, lastDigit) + " greater than 5")
elif lastDigit == 0:
    print(msg.format(number, lastDigit) + " 0")
elif lastDigit < 6:
    print(msg.format(number, lastDigit) + " less than 6 and not 0")
