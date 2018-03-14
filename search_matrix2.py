import pytest

class Solution():
    '''
    https://leetcode.com/problems/search-a-2d-matrix-ii/solution/
    '''
    def search_matrix(self, matrix, target):
        if matrix in [[[]], []] or not (matrix[0][0] <= target <= matrix[len(matrix)-1][len(matrix[0])-1]):
            return False
        row = len(matrix) - 1
        col = 0
        while row >= 0 and col <= len(matrix[0])-1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        (([
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
         ], 12), True),
         (([[]], 3), False),
         (([], 3), False),
         (([[2]], 3), False),
         (([[1, 2]], 2), True),
         (([[1, 2, 3]], 1), True),
         (([[2]], 2), True),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.search_matrix(*args) == result
