"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
class Solution:
    def trailingZeroes(self, n):
        '''
        Idea: https://discuss.leetcode.com/topic/6513/simple-c-c-solution-with-detailed-explaination
        '''
        base = 5
        zeros = 0
        while base <= n:
            zeros += n/base
            base *= 5
        return zeros

