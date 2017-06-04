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

    def rob(self, arr):
        """
        Idea:
            f(n) = max(f(n-1), f(n-2) + arr[n])
        """
        max_n_2, max_n_1 = 0, 0
        for cur_num in arr:
            cur_max = max(max_n_1, cur_num + max_n_2)
            max_n_2 = max_n_1
            max_n_1 = cur_max

        return max_n_1

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
