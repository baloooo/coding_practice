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

    def maxSubArray(self, arr):
        """
        Kadane's algorithm
        """
        global_max = current_max = arr[0]
        for index in xrange(1, len(arr)):
            current_max = max(arr[index], current_max+arr[index])
            global_max = max(current_max, global_max)
        return global_max

    def maxSubArray_with_indices(self, arr):
        """
        Kadane's algorithm
        https://stackoverflow.com/questions/14180308/finding-the-start-and-end-index-for-a-max-sub-array
        """
        global_max = current_max = arr[0]
        start = end = 0
        for index in xrange(1, len(arr)):
            if arr[index] > current_max+arr[index]:
                start = end = index
            current_max = max(arr[index], current_max+arr[index])
            global_max = max(current_max, global_max)
        return global_max, start, end

    def max_sub_array(self, arr):
        global_max = current_max = arr[0]
        i, j = 0, 0
        for index in xrange(1, len(arr)):
            # current_max = max(arr[index], current_max+arr[index])
            new_i, new_j = 0, 0
            if arr[index] > current_max+arr[index]:
                new_i = new_j = index
                current_max = arr[index]
            else:
                current_max = current_max+arr[index]
                new_i = i
                new_j = j + 1
            if global_max < current_max:
                i, j = new_i, new_j
                global_max = current_max
            # global_max = max(current_max, global_max)
        # optionally sends back array indexes also.
        return (global_max, (i, j))

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # arr = [100, -3, -4, -5, -2, 2]
    arr = [-1, -2, -3, -4]
    print Solution().max_sub_array(arr)
