"""
Given a set of non-negative integers, and a value sum, determine if there is a
subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
"""


class Solution:
    def __init__(self):
        pass

    def subset_sum(self, arr, arr_len, cur_sum):
        if cur_sum == 0:
            return True
        if arr_len < 0 and cur_sum > 0:
            return False
        if cur_sum < 0:
            return False
        return (self.subset_sum(arr, arr_len - 1, cur_sum) or
                self.subset_sum(arr, arr_len - 1, cur_sum-arr[arr_len-1]))

if __name__ == '__main__':
    arr, target_sum = [3, 34, 4, 12, 5, 2], 9
    print Solution().subset_sum(arr, len(arr), target_sum)
