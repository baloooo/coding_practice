"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

Idea: 
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/


/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
"""


class Solution:
    def __init__(self):
        pass

    def rotate_matrix(self, matrix):
        # matrix[::-1] makes a copy
        matrix.reverse()
        for row in xrange(len(matrix)):
            for col in xrange(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return matrix

if __name__ == '__main__':
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
    ]
    for test_case in test_cases:
        res = Solution().rotate_matrix(test_case[0][:])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
