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

    def uniquePathsWithObstacles_optimized(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        This is more intutive since this is broken in to more logical steps, the only
        down side is the space complexity is O(row_n*col_n) (incase we're not allowed to
        modify the existing array and have to take a copy of obstacleGrid) but for everything else
        this is more logical
        """
        if obstacleGrid[0][0] == 1: return 0 # you cannot go anwhere from start position
        row_n, col_n = len(obstacleGrid), len(obstacleGrid[0])
        # Step1: populate zeroth row, currently obstacleGrid depics obstacles after this population it would depict number of ways to reach an index (x,y) in it.
        for col in xrange(col_n):
            if obstacleGrid[0][col] == 0:
                obstacleGrid[0][col] = 1  # This now depicts number of ways you can reach this (x,y) pos'n
            else: # obstacle found, therefore no index in this row can be reached so populate that
                for j in xrange(col, col_n):
                    obstacleGrid[0][j] = 0  # Note: This zero is the number of ways
                break
        # Step 2: populate zeroth column
        for row in xrange(1, row_n): # Note: Here row starts from 1 since zeroth was aleready populated in above loop (this can cancel it's effect)
            if obstacleGrid[row][0] == 0:
                obstacleGrid[row][0] = 1
            else:
                for i in xrange(row, row_n):
                    obstacleGrid[i][0] = 0
                break
        # Step3: populate 1 to n for grid
        for row in xrange(1, row_n):
            for col in xrange(1, col_n):
                if obstacleGrid[row][col] == 1: # you cannot go thru this index so no need to calculate no. of ways you can reach this index since you can't go anywhere from here, instead put 0 here to depict this doesn't add anything to our no. of ways count.
                    obstacleGrid[row][col] = 0
                else:
                    obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
        return obstacleGrid[row_n-1][col_n-1]

if __name__ == '__main__':
    # print Solution().unique_paths(3, 3)
    obstacle_grid = [[0]]
    print Solution().unique_paths2(obstacle_grid)
