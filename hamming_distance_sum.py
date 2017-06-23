"""
Idea: https://discuss.leetcode.com/topic/72092/java-o-n-time-o-1-space/2
"""


class Solution:
    def __init__(self):
        pass

    def my_func(self, nums):
        # This will define the number of bits we'll have to scan in worst case.
        # 32 can be given as a default number in problem statement sometimes
        if not nums:
            return 0
        max_num = max(nums)
        count = 0
        while max_num:
            # k is the number of numbers which have current bit set out of n
            k = 0
            for index in xrange(len(nums)):
                k += (nums[index] & 1)
                nums[index] = nums[index] >> 1
            count += (k * (len(nums)-k))
            max_num = max_num >> 1
        return count

if __name__ == '__main__':
    test_cases = [
        ([4, 14, 2], 6),
        ([2, 4, 6], 8),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
