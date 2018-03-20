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
        LC article contains multiple sols.
        https://leetcode.com/articles/missing-number/
        """
	if not nums: return
        cur_xor = 0
        desired_xor = 0
        for num in nums:
            cur_xor = cur_xor ^ num
        for i in xrange(1, len(nums)+1): # range goes untill len(nums)+1 since current len(nums) is missing a number we're trying to find, therefore correct lenght is including that number so we add that.
            desired_xor = desired_xor ^ i
        return cur_xor ^ desired_xor
