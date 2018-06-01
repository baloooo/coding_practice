import pytest

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        https://leetcode.com/problems/search-a-2d-matrix/discuss/26204/Share-my-two-O(logm-+-logn)-solutions
        """
        import math
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:  # some optimization
            return False
        rows, cols = len(matrix)-1, len(matrix[0])-1
        start, end = 0, rows
        while start < end: # Find the row number
            # Notice that we'll have to use ceil value for mid since our binary search is a little different here
            # as explained below. Therefore to prevent infinite loop in case of rows having only one column we use the ceil values for mid.
            mid = start + int(math.ceil((end-start)/2.0))
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                start = mid # since target can be in matrix[mid][0] row also, therefore we can't to mid+1 here
            else:
                end = mid - 1 # since if we check with the first item on the row, anything less and we can safely skip the row.
        target_row = end  # start = end, so can use anyone
        start, end = 0, cols
        while start <= end:  # Use = sign here to test when there's only one row or column
            mid = start + (end-start)/2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        (([
		  [1,   3,  5,  7],
		  [10, 11, 16, 20],
		  [23, 30, 34, 50]
		], 3), True),
        (([[1]], 1), True),
        (([[1], [3]], 2), False),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.searchMatrix(*args) == result
