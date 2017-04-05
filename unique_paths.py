"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path_map = [[1 for col in xrange(n)] for row in xrange(m)]
        for cur_row in xrange(1, m):
            for cur_col in xrange(1, n):
                # Starts from (1,1)
                path_map[cur_row][cur_col] = path_map[cur_row-1][cur_col] + path_map[cur_row][cur_col-1]
        return path_map[m-1][n-1]
