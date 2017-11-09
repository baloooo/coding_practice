"""
Given a matrix of size M x N, there are large number of queries to find submatrix sums. Inputs to queries are left top and right bottom indexes of submatrix whose sum is to find out.

How to preprocess the matrix so that submatrix sum queries can be performed in O(1) time.
Idea: https://stackoverflow.com/questions/2277749/calculate-the-sum-of-elements-in-a-matrix-efficiently
"""


class Solution:
    def generate_summed_area_matrix(self, original_matrix):
        row_num = len(original_matrix)
        col_num = len(original_matrix[0])
        sat_matrix = [[0 for _ in xrange(col_num)] for _ in xrange(row_num)]
        for row in xrange(row_num):
            for col in xrange(col_num):
                sat_matrix[row][col] += original_matrix[row][col]
                if row-1 >= 0:
                    sat_matrix[row][col] += sat_matrix[row-1][col]
                if col-1 >= 0:
                    sat_matrix[row][col] += sat_matrix[row][col-1]
                if row-1 >=0 and col-1 >= 0:
                    sat_matrix[row][col] -= sat_matrix[row-1][col-1] # since [x-1][y-1] was added twice
        return sat_matrix

    def sub_matrix_sum(self, original_matrix, lx, ly, rx, ry):
        # (lx, ly) are top left coordinates of required rectangle(submatrix)
        # (rx, ry) are bottom right coordinates of required rectangle.
        # preprocess to create SAT (summed area table/matrix)
        # https://en.wikipedia.org/wiki/Summed_area_table
        sat_matrix = self.generate_summed_area_matrix(original_matrix)
        # check diagram here for more clarity https://stackoverflow.com/a/41884407/2795050
        sub_matrix_sum = sat_matrix[rx][ry]
        if ly - 1 >= 0:
            sub_matrix_sum -= sat_matrix[rx][ly-1]
        if lx -1 >= 0:
            sub_matrix_sum -= sat_matrix[lx-1][ry]
        if lx - 1 >=0 and ly -1 >= 0:
            sub_matrix_sum += sat_matrix[lx-1][ly-1]
        return sub_matrix_sum

if __name__ == '__main__':
    test_cases = [
        ([[1, 2, 3, 4, 6],
	[5, 3, 8, 1, 2],
	[4, 6, 7, 5, 5],
	[2, 4, 8, 9, 4]], [1, 2, 3, 3], 38),
    ]
    for test_case in test_cases:
        res = Solution().sub_matrix_sum(test_case[0], *test_case[1])
        if res == test_case[2]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[2])
