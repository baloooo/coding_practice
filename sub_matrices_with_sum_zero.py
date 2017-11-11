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
        '''
        Iterate over all pairs of rows. When fixing two rows r1 and r2, we can convert this to 1D version of the problem.

        When we have a 1D array ARR we want to find number of subarrays such that the sum of the elements in the subarray is equal to 0. To do that lets iterate from left to right, say we are currently at i-th element. If we have i-th prefix sum equal to sum(ARR[0..i]), then we want to find number of such j’s that sum(ARR[0..i]) = sum(ARR[0..j]). That means that the subarray ARR[j + 1..i] will have zero sum. To efficiently count number of such j’s we can use a HashMap (unordered_map in C++).

        In order to convert the problem to 1D, when we have a pair of fixed rows r1 and r2, we will keep a 2D prefix sums, let’s call it PRE (let’s also assume that initial matrix is A). PRE[i, j] will be the sum of elements in sub matrix whose upper left corner is [0, 0] and lower right corner is [i, j]. In other words it is a sum of all A[p, q] where 0 <= p <= i and 0 <= q <= j.
        The calculation of PRE is very easy: PRE[i, j] = A[i, j] + PRE[i - 1, j] + PRE[i, j - 1] - PRE[i - 1, j - 1] (if i - 1 or j - 1 are less than 0 then we just omit the terms where they appear). Notice, that we need to subtract PRE[i - 1, j - 1] since it is contained in both PRE[i - 1, j] and PRE[i, j - 1] and we want every element to appear in PRE[i, j] exactly once. This is called inclusion exclusion principle.

        When we have two fixed rows r1, r2 and have calculated PRE, we can obtain ARR. Note that we don’t really need to calculate each element of ARR, since we only need prefix sums of ARR, that is sum(ARR[0..i]) for each i. The sum(ARR[0..i]) is equal to PRE[r2][i] - PRE[r1 - 1][i] (if r1 - 1 < 0 then omit second operand). Being able to efficiently calculate sum(ARR[0..i]), let’s apply the 1D solution.

        The answer to the problem will be simply the sum of answers for all different pairs of rows.

        Overall time complexity is O(N3).
        Space complexity is O(N2)
        '''

    def solve(self, A):
            r = len(A)
            if r is 0:
                return 0
            c = len(A[0])
            if c is 0:
                return 0
            ans = 0
            pSum = [[0 for i in range(c+1)] for j in range(r + 1)] 

            for i in range(1, r + 1):
                for j in range(1, c + 1):
                    pSum[i][j] = A[i-1][j-1] + pSum[i-1][j] + pSum[i][j-1] - pSum[i-1][j-1]

            for  i in range(1, r + 1):
                for j in range(i, r + 1):
                    counti = {}
                    counti[0] = 1
                    for k in range(1, c + 1):
                        val = pSum[j][k] - pSum[i-1][k]
                        if val in counti:
                            ans = ans + counti[val]
                            counti[val] = counti[val] + 1
                        else:
                            counti[val] = 1
            return ans


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
