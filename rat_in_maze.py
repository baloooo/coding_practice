"""
A Maze is given as N*N binary matrix of blocks where source block is the upper
left most block i.e., maze[0][0] and destination block is lower rightmost block
i.e., maze[N-1][N-1]. A rat starts from source and has to reach destination.
The rat can move only in two directions: forward and down.
In the maze matrix, 0 means the block is dead end and 1 means the block can be
used in the path from source to destination. Note that this is a simple version
of the typical Maze problem. For example, a more complex version can be that
the rat can move in 4 directions and a more complex version can be with limited
number of moves.
"""


class Solution:
    def __init__(self, maze, final_x, final_y, max_row, max_col):
        self.maze = maze
        self.max_row = max_row
        self.max_col = max_col
        self.final_x = final_x
        self.final_y = final_y

    def path_exists_dp(self, cur_x, cur_y):
        # Time: O(mn) Space: O(mn)
        """
        Given a cost matrix cost[][] and a position (m, n) in cost[][], write
        a function that returns cost of minimum cost path to reach (m, n) from
        (0, 0). Each cell of the matrix represents a cost to traverse through
        that cell. Total cost of a path to reach (m, n) is sum of all the costs
        on that path (including both source and destination). You can only
        traverse down, right and diagonally lower cells from a given cell,
        i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1)
        can be traversed. You may assume that all costs are positive integers.
        """
        pass

    def path_exists_naive(self, cur_x, cur_y):
        # Time: O() Space: O(1)
        if cur_x == self.final_x and cur_y == self.final_y:
            return True
        if cur_x + 1 < self.max_col and self.maze[cur_x+1][cur_y]:
            if self.path_exists(cur_x + 1, cur_y):
                return True
        if cur_y + 1 < self.max_row and self.maze[cur_x][cur_y+1]:
            if self.path_exists(cur_x, cur_y + 1):
                return True
        return False

if __name__ == '__main__':
    test_case = ([
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 1],
    ], 3, 3, 0, 0)
    print Solution(test_case[0], test_case[1], test_case[2], len(test_case[0]),
                   len(test_case[0][0])).path_exists(
                        test_case[3], test_case[4])
