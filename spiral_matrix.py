"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution:

    def spiral(self, matrix):
        if not matrix:
            return []
        row_len = len(matrix)-1
        col_len = len(matrix[0])-1
        # initialize boundaries
        top_boundary, right_boundary, bottom_boundary, left_boundary = 0, col_len, row_len, 0
        spiral = []
        while(True):
            for cur_col in xrange(left_boundary, right_boundary+1):
                spiral.append(matrix[top_boundary][cur_col])
            top_boundary += 1
            if top_boundary > bottom_boundary: break
            for cur_row in xrange(top_boundary, bottom_boundary+1):
                spiral.append(matrix[cur_row][right_boundary])
            right_boundary -= 1
            if right_boundary < left_boundary: break
            for cur_col in xrange(right_boundary, left_boundary-1, -1):
                spiral.append(matrix[bottom_boundary][cur_col])
            bottom_boundary -= 1
            if bottom_boundary < top_boundary: break
            for cur_row in xrange(bottom_boundary, top_boundary-1, -1):
                spiral.append(matrix[cur_row][left_boundary])
            left_boundary += 1
            if left_boundary > right_boundary: break
        return spiral

if __name__ == '__main__':
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5])
    ]
    for test_case in test_cases:
        res = Solution().spiral(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])

"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""



class Solution2:
    def __init__(self):
        pass 

    class Solution2(object):
        def generateMatrix(self, n):
            """
            :type n: int
            :rtype: List[List[int]]
            """
            if not n:
                return []
            # initialize boundaries
            top_boundary, right_boundary, bottom_boundary, left_boundary = 0, n-1, n-1, 0
            spiral = [[0 for _ in xrange(n)] for _ in xrange(n)]
            num = 1
            while(True):
                for cur_col in xrange(left_boundary, right_boundary+1):
                    spiral[top_boundary][cur_col]=num
                    num += 1
                top_boundary += 1
                if top_boundary > bottom_boundary: break
                for cur_row in xrange(top_boundary, bottom_boundary+1): 
                    spiral[cur_row][right_boundary] = num
                    num += 1
                right_boundary -= 1
                if right_boundary < left_boundary: break
                for cur_col in xrange(right_boundary, left_boundary-1, -1): 
                    spiral[bottom_boundary][cur_col] = num
                    num += 1
                bottom_boundary -= 1
                if bottom_boundary < top_boundary: break
                for cur_row in xrange(bottom_boundary, top_boundary-1, -1): 
                    spiral[cur_row][left_boundary] = num
                    num += 1
                left_boundary += 1
                if left_boundary > right_boundary: break
            return spiral
if __name__ == '__main__':
    test_cases = [
        (3, [
         [ 1, 2, 3 ],
         [ 8, 9, 4 ],
         [ 7, 6, 5 ]
        ]),
    ]
    for test_case in test_cases:
        res = Solution2().spiral_matrix2(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])

