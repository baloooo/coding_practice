"""
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that
g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3
 NOTE : DO NOT USE LIBRARY FUNCTIONS
"""


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a<b:
        temp = a
        a = b
        b = temp
    while(1):
        remainder = a % b
        if remainder == 0:
            return b
        else:
            a = b
            b = remainder

if __name__ == '__main__':
    a, b = [10, 15]
    a, b = [55, 34]
    a, b = [121393, 75025]
    print gcd(a, b)
