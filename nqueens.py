# *-* coding:utf-8
"""
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
import copy


class Solution():
    """
    T(n) = n-1(T(n-1)) + O(n) which is O(n!)
    Idea: We can go row by row, and in each position, we need to check if the column, the 45° diagonal and the 135° diagonal had a queen before
    https://discuss.leetcode.com/topic/13617/accepted-4ms-c-solution-use-backtracking-and-bitmask-easy-understand
    Time:  
    Space: 
    """
    def is_valid(self, queens, row, col):
        '''
        checks cur row, cur col, 45 and 135 degree for collisions.
        '''
        for cur_row in xrange(row):
            if queens[cur_row][col] == 'Q': return False
        for cur_col in xrange(col):
            if queens[row][cur_col] == 'Q': return False
        for cur_row, cur_col in zip(xrange(row-1, -1, -1), xrange(col+1, len(queens))): # 135 degree
            if queens[cur_row][cur_col] == 'Q': return False
        for cur_row, cur_col in zip(xrange(row-1, -1, -1), xrange(col-1, -1, -1)):
            if queens[cur_row][cur_col] == 'Q': return False
        return True
        

    def get_nqueens(self, queens, res, row):
        if row == len(queens):
            # res.append(copy.deepcopy(queens))
            res.append([''.join(cur_row) for cur_row in queens])
            return
        for col in xrange(len(queens)):
            if self.is_valid(queens, row, col):
                queens[row][col] = 'Q'
                self.get_nqueens(queens, res, row + 1)
            queens[row][col] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        queens = [['.' for _ in xrange(n)] for _ in xrange(n)]
        self.get_nqueens(queens, res, 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 4
    for nqueen_combination in sol.solveNQueens(n):
        for each in nqueen_combination:
            print each
        print
