"""
https://discuss.leetcode.com/topic/5056/any-shorter-o-1-space-solution/2
Idea: Idea is simple: store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row0 and the state of column0 would occupy the same cell, I let it be the state of row0, and use another variable "col0" for column0. In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way.
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        Idea: https://discuss.leetcode.com/topic/5056/any-shorter-o-1-space-solution?page=1
        """
        # place markers at row and col beginnings.
        col0 = False
        for i in xrange(len(matrix)): # Pass 1
            if matrix[i][0] == 0: col0 = True
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # marks this row to be zeroed
                    matrix[0][j] = 0 # marks this col to be zeroed
        # Pass 2
        for i in xrange(len(matrix)-1, -1, -1):
            for j in xrange(len(matrix[0])-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0: matrix[i][0] = 0
                    

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
