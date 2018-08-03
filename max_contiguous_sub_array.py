"""
Max Sum Contiguous SubarrayBookmark Suggest Edit
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example:
Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
https://www.youtube.com/watch?v=86CQq3pKSUw
"""


class Solution:

    def max_sub_array(self, arr):
        """
        Kadane's algorithm
        """
        global_max = current_max = arr[0]
        for index in xrange(1, len(arr)):
            current_max = max(arr[index], current_max+arr[index])
            global_max = max(current_max, global_max)
        return global_max

    def max_sub_array_with_indices(self, arr):
        """
        Kadane's algorithm
        Flip is a intresting manifestation of the logic:
            https://discuss.leetcode.com/topic/149/flip/13
        """
        global_max = current_max = arr[0]
        start = end = 0
        for index in xrange(1, len(arr)):
            current_max = max(arr[index], current_max+arr[index])
            if current_max > global_max:
                if current_max == arr[index]:
                    start = end = index
                else:
                    end += 1
                global_max = current_max

        return global_max, start, end

if __name__ == '__main__':
    # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [100, -3, -4, -5, -2, 2]
    arr = [2, 4, -1, 5]
    arr = [10, 20, -5, -5, -5, -5, -5, -5, 5, 30]
    # arr = [-1, -2, -3, -4]
    print Solution().max_sub_array(arr)
    print Solution().max_sub_array_with_indices(arr)
