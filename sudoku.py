"""
[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
"""
class Solution():
    def solve_sudoku(self, sudoku_board):
        def is_valid(row, col):
            # check row
            for cur_col in xrange(9):
                if cur_col != col and sudoku_board[row][cur_col] == sudoku_board[row][col]:
                    return False
            # check col
            for cur_row in xrange(9):
                if cur_row != row and sudoku_board[cur_row][col] == sudoku_board[row][col]:
                    return False
            # check 3*3 board
            sudoku_set = set()
            row_start = row - (row % 3)
            col_start = col - (col % 3)
            for cur_row in xrange(3):
                for cur_col in xrange(3):
                    if sudoku_board[row_start + cur_row][col_start + cur_col] != '.' and sudoku_board[row_start + cur_row][col_start + cur_col] in sudoku_set:
                        return False
                    sudoku_set.add(sudoku_board[row_start + cur_row][col_start + cur_col])
	    return True
        # main solver
	def solver(sudoku_board):
	    for row in xrange(9):
		for col in xrange(9):
		    if sudoku_board[row][col] == '.':
			for new_val in xrange(1, 10):
			    sudoku_board[row][col] = str(new_val)
			    if is_valid(row, col) and solver(sudoku_board):
				return True
			    sudoku_board[row][col] = '.'
                        return False
	    return True
	solver(sudoku_board)

if __name__ == '__main__':
    sol = Solution()
    # sudoku_str = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
    sudoku_str = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
    sudoku_board = [list(sudoku_str[start: start+9]) for start in xrange(0, len(sudoku_str), 9)]
    sol.solve_sudoku(sudoku_board)
    print sudoku_board
