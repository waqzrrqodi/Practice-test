# Program that approximates eulers number
import math

def eulers_number(number):
    e = 0
    for n in range(0, number + 1):
        e += 1 / math.factorial(n)
    return e

print(eulers_number(700))