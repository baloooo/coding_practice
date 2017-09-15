'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        proper way of asking this
        Note: take care of the initial values for i and xor variables
        http://www.geeksforgeeks.org/find-the-missing-number/
        """
        i, xor = 0, 0
        for i in xrange(len(nums)):
            # XOR is distributive and a^b^b is a
            xor = xor ^ i ^ nums[i]
        # Following xor is because [0, 1] should ouput 2 as by definition one number is always
        # missing 
        return xor ^ i+1

