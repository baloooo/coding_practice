"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, n):
        base = 5
        zeros = 0
        while base <= n:
            zeros += n/base
            base *= 5
        return zeros

