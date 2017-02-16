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


class Solution():
    def __init__(self):
        self.possible_arrangements = []
        self.cur_arrng = []

    def possible_nqueens(self, n):
        from copy import deepcopy
        def no_conflicting_queen(row, col):
            # check column
            for cur_row in xrange(row+1):
                if self.cur_arrng[cur_row][col] == 'Q':
                    return False
            # check row
            for cur_col in xrange(col+1):
                if self.cur_arrng[row][cur_col] == 'Q':
                    return False
            # check diagonal
            # top left
            cur_row, cur_col = row, col
            while(cur_row >= 0 and cur_col >= 0):
                if self.cur_arrng[cur_row][cur_col] == 'Q':
                    return False
                cur_row -= 1
                cur_col -= 1
            # top right
            cur_row, cur_col = row, col
            while(cur_row >= 0 and cur_col < n):
                if self.cur_arrng[cur_row][cur_col] == 'Q':
                    return False
                cur_row -= 1
                cur_col += 1
            return True

        def nqueen(row):
            if row == n:
                self.possible_arrangements.append(deepcopy(self.cur_arrng))
            else:
                for col in xrange(n):
                    if no_conflicting_queen(row, col):
                        self.cur_arrng[row][col] = 'Q'
                        nqueen(row+1)
                        self.cur_arrng[row][col] = '.'
        if n < 1:
            return []
        self.cur_arrng = [['.']*n for _ in xrange(n)]
        nqueen(0)
        result = [[''.join(each) for each in combination] for combination in self.possible_arrangements]
        if len(result) == 1:
            return result[0]
        return result

if __name__ == '__main__':
    sol = Solution()
    n = 4
    for nqueen_combination in sol.possible_nqueens(n):
        for each in nqueen_combination:
            print each
        print
