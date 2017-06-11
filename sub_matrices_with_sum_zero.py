"""
Given a 2D matrix, find the number non-empty sub matrices, such that the sum of
the elements inside the sub matrix is equal to 0. (note: elements might be
negative).

Example:

Input

-8 5  7
3  7 -8
5 -8  9
Output
2
map = {0: 0, 4:1, 8:2}

Explanation
-8 5 7
3 7 -8
5 -8 9

-8 5 7
3 7 -8
5 -8 9
"""


class Solution:

    def sub_matrices_sum_zero_with_dp(self, matrix):
        # Time: O(n^2) no. of unique sub matrices
        # Space: O(n^2) no. of unique sub matrices
        count = 0
        row = len(matrix)
        col = len(matrix[0])
        matrix_sum_map = {}
        for i in xrange(row):
            for j in xrange(i, row):
                for m in xrange(col):
                    for n in xrange(m, col):
                        matrix_sum = 0
                        for row_index in xrange(i, j+1):
                            for col_index in xrange(m, n+1):
                                matrix_sum += matrix[row_index][col_index]
                        if matrix_sum == 0:
                            count += 1
        return count
    def sub_matrices_sum_zero_without_dp(self, matrix):
        # Time: O(n^6)
        count = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in xrange(row):
            for j in xrange(i, row):
                for m in xrange(col):
                    for n in xrange(m, col):
                        matrix_sum = 0
                        for row_index in xrange(i, j+1):
                            for col_index in xrange(m, n+1):
                                matrix_sum += matrix[row_index][col_index]
                        if matrix_sum == 0:
                            count += 1
        return count

    def print_all_submatrices_op(self, matrix):
        # Time: O(n^4) for generating and O(n^2) for printing therefore O(n^6)
        # same as below, just with better variable names
        row_num = len(matrix)
        col_num = len(matrix[0])
        # matrices = set()
        for start_row in xrange(row_num):
            for cur_start_row in xrange(row_num):
                for start_col in xrange(col_num):
                    for cur_start_col in xrange(start_col, col_num):
                        print '-'*10
                        for row in xrange(cur_start_row, row_num):
                            for col in xrange(cur_start_col, col_num):
                                print matrix[row][col],
                                # matrices.add(matrix[row][col])
                            print
        # return matrices


    # def print_all_submatrices(self, matrix):
    #     # Time: O(n^4) for generating and O(n^2) for printing therefore O(n^6)
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     matrices = set()
    #     for i in xrange(row):
    #         for j in xrange(i, row):
    #             for m in xrange(col):
    #                 for n in xrange(m, col):
    #                     # print "-"*10
    #                     for row_index in xrange(i, j+1):
    #                         for col_index in xrange(m, n+1):
    #                             # print matrix[row_index][col_index],
    #                             matrices.add(matrix[row_index][col_index])
    #                         # print
    #     return matrices

if __name__ == '__main__':
    test_case = [[-8, 5, 7], [3, 7, -8], [5, -8,  9]]
    print Solution().print_all_submatrices_op(test_case)
    # test_case = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print Solution().sub_matrices_sum_zero(test_case)
