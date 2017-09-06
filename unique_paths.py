"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in
the diagram below).

How many possible unique paths are there?
"""


class Solution(object):

    def find_unique_paths_bruteforce_main(self, x, y, m, n):
        """
        Time: O((m+n)!/m!n!)
        https://stackoverflow.com/questions/17207266/robot-moving-in-a-grid-algorithm-possible-paths-and-time-complexity
        https://stackoverflow.com/questions/11607376/which-function-grows-faster-exponential-or-factorial
        Space: O(max(m, n))
        """
        if x > m or y > n:
            return 0
        if x == m-1 and y == n-1:
            return 1
        return(self.find_unique_paths(x+1, y, m, n) +
               self.find_unique_paths(x, y+1, m, n))

    def unique_paths_bruteforce(self, m, n):
        self.unique_paths_bruteforce = 0
        self.find_unique_paths_bruteforce_main(0, 0, m, n)
        return self.unique_paths_bruteforce

    def unique_paths(self, m, n):
        """
        Time: O(m*n)
        Space: O(m*n)
        """
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

    def unique_paths_dp(self, obstacle_grid):
        """
        Time: O(m*n)
        Space: O(m*n)
        """
        col = len(obstacle_grid[0])
        row = len(obstacle_grid)
        dp = [[0 for _ in xrange(col+1)] for _ in xrange(row+1)]
        """
        Not sure completely: This is just a trick:
        We've included an extra row and col. So what we're essentially trying
        to acheive here is that we want to start the count since all values
        are initialized to zero this one will kick start the count.
        """
        dp[0][1] = 1
        for i in xrange(1, row+1):
            for j in xrange(1, col+1):
                if obstacle_grid[i-1][j-1] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row][col]

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
