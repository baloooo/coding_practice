'''
Base logic almost identical to max_sum_rectangle, just instead of kadane we'll have to use
zero_sum_largest_subarray since we're not looking for lagest sum subarray which kadane provides.
'''


class Solution:
    def zero_sum_largest_subarray(self, arr):
        cur_sum, max_len, start = 0, 0, 0
        sum_map = {}
        for index, ele in enumerate(arr):
            cur_sum += ele
            if cur_sum == 0:
                # If the running sum reaches zero from the beginning of the array, the longest zero-sum subarray consists of the entire array till the index we reached
                max_len = index + 1
                start = 0
            if cur_sum in sum_map:
                cur_len = index-sum_map[cur_sum]
                if max_len < cur_len:
                    max_len = cur_len
                    start = sum_map[cur_sum]+1
            else:
                sum_map[cur_sum] = index
        cur_sum = sum(arr[start: start+max_len])
        return not bool(cur_sum), start, start+max_len-1

    def max_zero_sum_rectangle(self, arr):
        # Time: O(n^3)
        row_len, col_len = len(arr), len(arr[0])
        max_ele = -float('inf')
        final_left = final_right = final_top = final_bottom = 0

        for left in xrange(col_len):
            row_sum = [0]*row_len
            for right in xrange(left, col_len):
                # calculate sum b/w left and right for every row
                for row in xrange(row_len):
                    row_sum[row] += arr[row][right]
                cur_sum, row_start, row_end = self.zero_sum_largest_subarray(row_sum)
                cur_max_ele = (row_end - row_start + 1) * (right - left + 1)
                if cur_sum and cur_max_ele > max_ele:
                    max_ele, final_left, final_right = cur_max_ele, left, right
                    final_top, final_bottom = row_start, row_end

        for row in xrange(final_top, final_bottom+1):
            for col in xrange(final_left, final_right+1):
                print arr[row][col],
            print
        return [max_ele, final_left, final_right, final_top, final_bottom]

if __name__ == '__main__':
    arr = [
            [9, 7, 16, 5],
            [1, -6, -7, 3],
            [1, 8, 7, 9],
            [7, -2, 0, 10]
        ]
    test_cases = [
        (arr, ['dummy']),
    ]
    for test_case in test_cases:
        res = Solution().max_zero_sum_rectangle(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
