#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ldgt = abs(number) % 10
if number < 0:
    ldgt = -ldgt

if ldgt >= 5:
    print("Last digit of", number, "is", ldgt, "and is greater than 5")
elif ldigit == 0:
    print("Last digit of", number, "is", ldgt, "and is 0")
else:
    print("Last digit of", number, "is", ldgt, "and is less than 6 and not 0")
