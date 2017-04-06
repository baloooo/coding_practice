"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in
the diagram below).

How many possible unique paths are there?
"""


class Solution(object):
    def unique_paths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path_map = [[0 for col in xrange(n)] for row in xrange(m)]
        # preprocess path_map
        for col in xrange(n):
            path_map[0][col] = 1
        for row in xrange(m):
            path_map[row][0] = 1
        for cur_row in xrange(1, m):
            for cur_col in xrange(1, n):
                # Starts from (1,1)
                path_map[cur_row][cur_col] = path_map[cur_row-1][cur_col] + path_map[cur_row][cur_col-1]  # noqa
        return path_map[m-1][n-1]

    def unique_paths2(self, obstacle_grid):
        """
        Follow up for "Unique Paths":

        Now consider if some obstacles are added to the grids.
        How many unique paths would there be?

        An obstacle and empty space is marked as 1 and 0 respectively in the
        grid.

        For example,
        There is one obstacle in the middle of a 3x3 grid as illustrated below.

        [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
        The total number of unique paths is 2.
        """
        row_len = len(obstacle_grid)
        col_len = len(obstacle_grid[0])
        obstacle_grid[0][0] = 1 - obstacle_grid[0][0]
        for col in xrange(1, col_len):
            if obstacle_grid[0][col] == 1:
                obstacle_grid[0][col] = 0
            else:
                obstacle_grid[0][col] = obstacle_grid[0][col-1]
        for row in xrange(1, row_len):
            if obstacle_grid[row][0] == 1:
                obstacle_grid[row][0] = 0
            else:
                obstacle_grid[row][0] = obstacle_grid[row-1][0]
        for cur_row in xrange(1, row_len):
            for cur_col in xrange(1, col_len):
                if obstacle_grid[cur_row][cur_col] == 1:
                    obstacle_grid[cur_row][cur_col] = 0
                else:
                    obstacle_grid[cur_row][cur_col] = obstacle_grid[cur_row-1][cur_col] + obstacle_grid[cur_row][cur_col-1]  # noqa
        return obstacle_grid[row_len-1][col_len-1]

if __name__ == '__main__':
    # print Solution().unique_paths(3, 3)
    obstacle_grid = [[0]]
    print Solution().unique_paths2(obstacle_grid)
