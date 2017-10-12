"""
[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
"""


class Solution(object):
    """
    Time: n^m where n is the number of possibilities for each square (i.e., 9 in classic Sudoku)
    and m is the number of spaces that are blank.
    Space: O(m) as can only go to 'm' level deep
    https://stackoverflow.com/questions/15327376/algorithm-complexity-big-o-of-sudoku-solver
    """
    def is_valid(self, board, cur_row, cur_col, cur_num):
        """
        Observation:
        base_row_index = 3*(row/3) Notice here don't cancel 3's here, this is integer division
        For ex: for row=1 base_row_index would be 0 and not 1 which you would get if you cancel
        3's.
        base_col_index = 3*(col/3)
        row_offset = index / 3
        col_offset = index % 3
        """
        for index in xrange(9):
            if index != cur_col and board[cur_row][index] == cur_num: return False
            if index != cur_row and board[index][cur_col] == cur_num: return False
            if board[3*(cur_row/3)+index/3][3*(cur_col/3)+index%3] == cur_num: return False
        return True

    def solve_sudoku(self, board, start_row, start_col):
        for cur_row in xrange(start_row, len(board)):
            start_col = 0
            for cur_col in xrange(start_col, len(board)):
                if board[cur_row][cur_col] == '.':
                    for cur_num in '123456789':
                        if self.is_valid(board, cur_row, cur_col, cur_num):
                            board[cur_row][cur_col] = cur_num
                            if self.solve_sudoku(board, cur_row, cur_col+1):
                                return board
                            else:
                                board[cur_row][cur_col] = '.'
                    return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        Idea: https://discuss.leetcode.com/topic/11327/straight-forward-java-solution-using-backtracking/33
        """
        board = [list(row) for row in board]
        return self.solve_sudoku(board, 0, 0)

if __name__ == '__main__':
    sol = Solution()
    # sudoku_str = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
    # sudoku_str = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
    # sudoku_board = [list(sudoku_str[start: start+9]) for start in xrange(0, len(sudoku_str), 9)]
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    print sol.solveSudoku(board)
