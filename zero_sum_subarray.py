"""
Given an unsorted array of integers, find a continous subarray
which adds to a given number.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There may be more than one subarrays with sum as the given sum. The following
solutions print first such subarray.
"""


class Solution:
    def __init__(self):
        pass

    def k_sum_subarray_with_negative(arr):
        # Time: O(n) Space: O(n)
        pass

    def k_sum_subarray_without_negative(self, arr, target_sum):
        # No negative values in inp_arr
        for i in xrange(len(arr)):
            for j in xrange(len(arr)):
                if sum(arr[i:j+1]) == target_sum:
                    return (i, j)
        return -1


if __name__ == '__main__':
    arr = [4, 2, 3, 1, 6]
    print Solution().k_sum_subarray_without_negative(arr, 7)
