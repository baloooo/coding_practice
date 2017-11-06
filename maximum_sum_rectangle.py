'''
http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/
'''


class Solution:
    def kadane(self, arr):
        # max_so_far = -float('inf')
        # max_ending_here = start = cur_start = end = 0
        # for index, ele in enumerate(arr):
        #     max_ending_here += ele
        #     if max_ending_here > max_so_far:
        #         max_so_far = max_ending_here
        #         start = cur_start
        #         end = index
        #     if max_ending_here < 0:
        #         max_ending_here = 0
        #         cur_start = index + 1
        # return max_so_far, start, end

        global_max = cur_max = arr[0]
        start = end = 0
        for index in xrange(1, len(arr)):
            cur_max = max(arr[index], cur_max+arr[index])
            if cur_max > global_max:
                if cur_max == arr[index]:
                    start = end = index
                else:
                    end += 1
                global_max = cur_max
        return global_max, start, end

    def max_sum_rectangle(self, arr):
        # Time: O(n^3)
        row_len, col_len = len(arr), len(arr[0])
        max_sum = -float('inf')
        final_left = final_right = final_top = final_bottom = 0

        for left in xrange(col_len):
            row_sum = [0]*row_len
            for right in xrange(left, col_len):
                # calculate sum b/w left and right for every row
                for row in xrange(row_len):
                    row_sum[row] += arr[row][right]
                cur_sum, row_start, row_end = self.kadane(row_sum)
                if cur_sum > max_sum:
                    max_sum, final_left, final_right = cur_sum, left, right
                    final_top, final_bottom = row_start, row_end

        for row in xrange(final_top, final_bottom+1):
            for col in xrange(final_left, final_right+1):
                print arr[row][col],
            print
        return [max_sum, final_left, final_right, final_top, final_bottom]

if __name__ == '__main__':
    arr = [
            [1,   2, -1, -4, -20],
            [-8, -3,  4,  2,   1],
            [3,   8, 10,  1,   3],
            [-4, -1,  1,  7,  -6]
        ]
    test_cases = [
        (arr, [29, 1, 3, 1, 3]),
    ]
    for test_case in test_cases:
        res = Solution().max_sum_rectangle(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
