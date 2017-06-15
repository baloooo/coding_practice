

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
