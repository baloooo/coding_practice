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
    T(n) = n-1(T(n-1)) + O(n) which is O(n^n), therefore exponential.
    Idea: n this problem, we can go row by row, and in each position, we need to check if the column, the 45° diagonal and the 135° diagonal had a queen before
    https://discuss.leetcode.com/topic/13617/accepted-4ms-c-solution-use-backtracking-and-bitmask-easy-understand
    Time:  
    Space: 
    """
    class Solution(object):
    def valid_n_queen(self, n_queen_matrix, row, col, n):
        # check all columns up to cur_row (as below rows are not filled untill now so no need to check them)
        for cur_row in xrange(row):
            if n_queen_matrix[cur_row][col] == 'Q':
                return False
        # check if the 45° diagonal had a queen before.
        cur_col = col+1
        for cur_row in xrange(row-1, -1, -1):
            if cur_col >= n:
                break
            if n_queen_matrix[cur_row][cur_col] == 'Q':
                return False
            cur_col += 1
        # check if the 135° diagonal had a queen before.
        cur_col = col-1
        for cur_row in xrange(row-1, -1, -1):
            if cur_col < 0 :
                break
            if n_queen_matrix[cur_row][cur_col] == 'Q':
                return False
            cur_col -= 1
        return True
            

    def solve_n_queens(self, n_queen_matrix, row, n):
        if row == n:
            self.feasible_combntns.append(copy.deepcopy(n_queen_matrix))
        else:
            for cur_col in xrange(n):
                n_queen_matrix[row][cur_col] = 'Q'
                if self.valid_n_queen(n_queen_matrix, row, cur_col, n):
                    self.solve_n_queens(n_queen_matrix, row+1, n)
                n_queen_matrix[row][cur_col] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.feasible_combntns = []
        n_queen_matrix = [['.']*n for _ in xrange(n)]
        self.solve_n_queens(n_queen_matrix, 0, n)
        return [[''.join(row) for row in nqueen] for nqueen in self.feasible_combntns]


if __name__ == '__main__':
    sol = Solution()
    n = 4
    for nqueen_combination in sol.solveNQueens(n):
        for each in nqueen_combination:
            print each
        print
