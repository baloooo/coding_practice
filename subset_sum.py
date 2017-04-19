"""
Given a set of non-negative integers, and a value sum, determine if there is a
subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
"""


class Solution:
    def __init__(self):
        pass

    def subset_sum_recursion(self, arr, arr_len, cur_sum):
        if cur_sum == 0:
            return True
        if arr_len < 0 and cur_sum > 0:
            return False
        if cur_sum < 0:
            return False
        return (self.subset_sum_recursion(arr, arr_len - 1, cur_sum) or
                self.subset_sum_recursion(arr, arr_len - 1,
                                          cur_sum-arr[arr_len-1]))

    def subset_sum_dp(self, arr, target_sum):
        # dp[i][j] can we make cur_sum (i) using numbers 0 to j-1
        # dp = [i (cur_sum)][numbers 0 ... j-1]
        dp = [[False for _ in xrange(len(arr)+1)] for _ in xrange(target_sum+1)]  # noqa
        for i in xrange(target_sum+1):
            dp[i][0] = False
        for j in xrange(len(arr)+1):
            dp[0][j] = True
        for cur_sum in xrange(1, target_sum+1):
            for cur_ele in xrange(1, len(arr)+1):
                dp[cur_sum][cur_ele] = dp[cur_sum][cur_ele-1]
                # cur_sum >= cur_element as only then can we try to make cur_sum using cur_element.  # noqa
                if cur_sum >= arr[cur_ele-1]:
                    dp[cur_sum][cur_ele] = dp[cur_sum][cur_ele] or dp[cur_sum - arr[cur_ele-1]][cur_ele-1]  # noqa
        return dp[target_sum][len(arr)]

if __name__ == '__main__':
    arr, target_sum = [3, 34, 4, 12, 5, 2], 9
    print Solution().subset_sum_recursion(arr, len(arr), target_sum)
    print Solution().subset_sum_dp(arr, target_sum)
