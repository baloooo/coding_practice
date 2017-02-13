# coding: utf-8
"""
The Sudoku board could be partially filled, where empty cells are filled with
the character ‘.’.
The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6",
".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

 Note:
 A valid Sudoku board (partially filled) is not necessarily solvable.
 Only the filled cells need to be validated.
 Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


def valid_sudoku(sudoku):
    # scan in row major order
    for row in sudoku:
        row_num = set()
        for num in row:
            if num == '.':
                continue
            if num not in row_num:
                row_num.add(num)
            else:
                return 0
    # scan in column major
    for index in xrange(9):
        col_num = set()
        for row in sudoku:
            num = row[index]
            if num == '.':
                continue
            if num not in col_num:
                col_num.add(row[index])
            else:
                return 0
    # scan for 3*3 boxes
    for row_index in xrange(9, 3):
        for col_index in xrange(9, 3):
            box_num = set()
            for row in xrange(row_index, row_index+4):
                for col in xrange(col_index, col_index+4):
                    num = sudoku[row_index][col_index]
                    if num == '.':
                        continue
                    if num not in box_num:
                        box_num.add(sudoku[row_index][col_index])
                    else:
                        return 0
    return 1

if __name__ == '__main__':
    sudoku = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
              "7...2...6", ".6....28.", "...419..5", "....8..79"]
    print valid_sudoku(sudoku)
