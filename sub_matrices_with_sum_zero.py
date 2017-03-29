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
    def __init__(self):
        pass

    def sub_matrices_sum_zero(matrix):
        for row in matrix:
            for col in row:

if __name__ == '__main__':
    matrix = [[-8, 5, 7], [3, 7, -8], [5, -8,  9]]
    print Solution().sub_matrices_sum_zero(matrix)
