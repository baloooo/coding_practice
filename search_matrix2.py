import pytest

class Solution():
    '''
    https://leetcode.com/problems/search-a-2d-matrix-ii/solution/
	We can start from top right also using the same broad approach:
	https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66139/6-9-lines-C++Python-Solutions-with-Explanations
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

############################################################################################################

	def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0])-1 if vertical else len(matrix)-1

        while hi >= lo:
            mid = (lo + hi)//2
            if vertical: # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        
        return False

    def searchMatrix_lessoptimal(self, matrix, target):
		'''
		https://leetcode.com/articles/search-a-2d-matrix-ii/
		An alternate way of solving by just riding on problem statement.
		O(log(n!)) or nlogn(proof https://stackoverflow.com/questions/2095395/is-logn-%CE%98n-logn)
		'''
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))): # As the shorter dimension define the len of diagonal
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        
        return False

############################################################################################################

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
