"""
Idea:
    https://discuss.leetcode.com/topic/15269/10-lines-28ms-o-n-space-dp-solution-in-c-with-explanations
    can be optimized to O(m) space rather than O(m*n) space.
"""


class Solution:
    def __init__(self):
        pass

    def min_path_sum(self, matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        dp = [[0 for _ in xrange(col_len)] for _ in xrange(row_len)]
        # sum first row
        dp[0][0] = matrix[0][0]
        for col in xrange(1, col_len):
            dp[0][col] = matrix[0][col] + dp[0][col-1]
        # sum first col
        for row in xrange(1, row_len):
            dp[row][0] = matrix[row][0] + dp[row-1][0]
        # apply algo starting from first row, first col
        for row in xrange(1, row_len):
            for col in xrange(1, col_len):
                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + matrix[row][col]  # noqa
        return dp[row_len-1][col_len-1]


if __name__ == '__main__':
    matrix = [
      [1, 2, 3],
      [4, 8, 2],
      [1, 5, 3]
    ]
    test_cases = [
        (matrix, 11),
    ]
    for test_case in test_cases:
        res = Solution().min_path_sum(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
