"""
https://discuss.leetcode.com/topic/5056/any-shorter-o-1-space-solution/2
Idea: Idea is simple: store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row0 and the state of column0 would occupy the same cell, I let it be the state of row0, and use another variable "col0" for column0. In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way.
"""


class Solution:
    def __init__(self):
        pass

    def set_matrix_zero(self, matrix):
        # should column 0 be made all zeros
        col0 = 1
        for row in xrange(len(matrix)):
            # If any row of column zero is zero set col0
            if matrix[row][0] == 0:
                col0 = 0
            for col in xrange(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0
        # start setting from bottom up way
        for row in xrange(len(matrix)-1, 0, -1):
            # last statement sets the column value so run
            # the loop untill column 1
            for col in xrange(len(matrix[0])-1, 0, -1):
                # import ipdb; ipdb.set_trace()
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if col0 == 0:
                matrix[row][0] = 0
        return matrix

if __name__ == '__main__':
    test_cases = [
        # ([[1, 0, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [1, 0, 1], [1, 0, 1]]),
        # ([[0]], [[0]]),
        ([[1, 1, 1], [0, 1, 2]], [[0, 1, 1], [0, 0, 0]])
    ]
    for test_case in test_cases:
        res = Solution().set_matrix_zero(test_case[0][:])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
