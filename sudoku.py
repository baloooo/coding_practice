"""
[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
"""
# class Solution():
#     def solve_sudoku(self, sudoku_board):
#         def is_valid(row, col):
#             # check row
#             for cur_col in xrange(9):
#                 if cur_col != col and sudoku_board[row][cur_col] == sudoku_board[row][col]:
#                     return False
#             # check col
#             for cur_row in xrange(9):
#                 if cur_row != row and sudoku_board[cur_row][col] == sudoku_board[row][col]:
#                     return False
#             # check 3*3 board
#             sudoku_set = set()
#             row_start = row - (row % 3)
#             col_start = col - (col % 3)
#             for cur_row in xrange(3):
#                 for cur_col in xrange(3):
#                     if sudoku_board[row_start + cur_row][col_start + cur_col] != '.' and sudoku_board[row_start + cur_row][col_start + cur_col] in sudoku_set:
#                         return False
#                     sudoku_set.add(sudoku_board[row_start + cur_row][col_start + cur_col])
# 	    return True
#         # main solver
# 	def solver(sudoku_board):
# 	    for row in xrange(9):
# 		for col in xrange(9):
# 		    if sudoku_board[row][col] == '.':
# 			for new_val in xrange(1, 10):
# 			    sudoku_board[row][col] = str(new_val)
# 			    if is_valid(row, col) and solver(sudoku_board):
# 				return True
# 			    sudoku_board[row][col] = '.'
#                         return False
# 	    return True
# 	solver(sudoku_board)


class Solution(object):
    def is_valid(self, board, cur_row, cur_col, cur_num):
        """
        Observation:
        base_row_index = 3*(row/3) Notice here don't cancel 3's here, this is integer division
        For ex: for row=1 base_row_index would be 0 and not 1 which you would get if you cancel
        3's.
        base_col_index = 3*(col/3)
        row_offset = i/3
        col_offset = i%3
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
        # for i in xrange(len(board)):
        #     for j in xrange(len(board[0])):
        #         if board[i][j] == '.':
        #             for c in '123456789':
        #                 if self.is_valid(board, i, j, c):
        #                     board[i][j] = c
        #                     if self.solve_sudoku(board):
        #                         return board
        #                     else:
        #                         board[i][j] = '.'
        #             return False
        # return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        Idea: https://discuss.leetcode.com/topic/11327/straight-forward-java-solution-using-backtracking/33
        """
        # board = [int(ele) for row in board for ele in row if ele!= '.']
        # res = []
        # for row in board:
        #     temp = []
        #     for ele in row:
        #         if ele != '.':
        #             ele = int(ele)
        #         temp.append(ele)
        #     res.append(temp)
        # board = res
        # print board
        board = [list(row) for row in board]
        return self.solve_sudoku(board, 0, 0)
        # return self.solve_sudoku(board)

if __name__ == '__main__':
    sol = Solution()
    # sudoku_str = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
    # sudoku_str = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
    # sudoku_board = [list(sudoku_str[start: start+9]) for start in xrange(0, len(sudoku_str), 9)]
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    print sol.solveSudoku(board)
