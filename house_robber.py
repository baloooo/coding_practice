"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
"""


class Solution:
    """
    https://discuss.leetcode.com/topic/17199/python-solution-3-lines/2
    https://discuss.leetcode.com/topic/11110/c-1ms-o-1-space-very-simple-solution
    """
    def __init__(self):
        pass

    def rob(self, arr):
        """
        Idea:
            f(0) = arr[0]
            f(1) = max(arr[0], arr[1])
            f(n) = max(f(n-1), f(n-2) + arr[n])
        """
        if not arr:
            return 0
        max_n_2 = arr[0]
        if len(arr) == 1:
            return max_n_2
        max_n_1 = arr[1]
        max_so_far = max(max_n_1, max_n_2)
        for cur_index in xrange(2, len(arr)):
            max_so_far = max(max_n_1, max_n_2+arr[cur_index])
        return max_so_far
        for num in arr:
            last = now
            now = max(num+last, now)
        reutrn now

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
