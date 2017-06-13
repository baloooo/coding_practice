"""
Given a 2D array, find the maximum sum subarray in it. For example, in the
following 2D array, the maximum sum subarray is highlighted with blue rectangle
and sum of this subarray is 29.
{
    {1, 2, -1, -4, -20},
    {-8, -3, 4, 2, 1},
    {3, 8, 10, 1, 3},
    {-4, -1, 1, 7, -6}
}
Idea:
    Prefix_sum + kadane's algo
    https://www.youtube.com/watch?v=yCQN096CwWM
    https://stackoverflow.com/a/18220549/2795050
    http://www.algorithmist.com/index.php/UVa_108
Add indices to kadane's max and complete max_sum_subarr, extend it for
max_one's subarr.
"""


class Solution:
    def __init__(self):
        pass

    def kadane_max(self, arr):
        """
        returns start and end index of max sub array.
        """
        cur_max = global_max = arr[0]
        start = end = 0
        for index in xrange(1, len(arr)):
            cur_max = max(arr[index], cur_max+arr[index])
            global_max = max(cur_max, global_max)
        return global_max

    def max_sum_subarray(self, arr):
        row_len = len(arr)
        col_len = len(arr[0])
        kadane_row = []
        max_sum_until_now = cur_max = -float('inf')
        max_left = max_right = max_up = max_down = 0
        for start_col in xrange(col_len):
            # kadane_row = [arr[row][start_col] for row in xrange(row_len)]
            kadane_row = [0]*row_len
            # max_up, max_down = self.kadane_max(kadane_row)
            for end_col in xrange(start_col, col_len):
                for row in xrange(row_len):
                    kadane_row[row] += arr[row][end_col]
                cur_max_sum, cur_max_up, cur_max_down = self.kadan_max(
                    kadane_row)
                if cur_max > max_sum_until_now:
                    max_sum_until_now = cur_max_sum
                    max_left = start_col
                    max_right = end_col
                    max_up = cur_max_up
                    max_down = cur_max_down
        print max_sum_until_now, max_left, max_right, max_up, max_down

if __name__ == '__main__':
    arr = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6]
    ]
    test_cases = [
        (arr, 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
