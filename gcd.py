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
class Solution(object):
    def gcd(self, x, y):
        # https://www.youtube.com/watch?v=JUzYl1TYMcU
        if x == 0:
            return y
        if y == 0:
            return x
        while x!=y:
            if x > y:
                x = x-y
            else:
                y = y-x
        return x
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        if x == z or y == z or x+y == z:
            return True
        return z % self.gcd(x,y) == 0

def gcd_euclidean(a, b):
    '''
    # https://leetcode.com/problems/water-and-jug-problem/description/
    is a nice example w/ sol here https://discuss.leetcode.com/topic/49238/math-solution-java-solution/31
    '''
    if a == 0: return b
    if b == 0: return a
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a



if __name__ == '__main__':
    test_cases = [[10, 15], [55, 34], [121393, 75025]]
    for each in test_cases:
        print gcd(*each)
        print gcd_euclidean(*each)


