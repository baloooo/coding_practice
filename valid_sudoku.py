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
class Solution:
    def valid_sudoku(self, board):
        '''
        There are two ways to go about it, one is the method at the bottom of the file here, where
        we run O(n^2) loop for each row in board, for each col in board and each box in board.
        Total: O(n^2) + O(n^2) + O(n^2), we can reduce this to just one O(n^2) by taking 
        "BOOLEAN" O(3*(n^2)) space.
        '''
        if not board:return False
        m,n=len(board),len(board[0])
        '''
        three 2d array to check each row, col and sub box
        Here each row in this 2d matrix will try to put True on indexes 0-8 and if for
        any row there is already a True means number is repeated. Notice having three
        separate arrays help in putting one value in 3 spaces helps to check if cur number
        has been encountered for this row, col, or box before.
        '''
        check_row=[[False for i in range(9)] for j in range(9)]
        check_col=[[False for i in range(9)] for j in range(9)]
        check_box=[[False for i in range(9)] for j in range(9)]
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] != '.':
                    num = int(board[i][j])-1  # need -1 becasue the index of array is 0~8
                    k = i/3*3 + j/3
                    '''
                    i, j, k are the row numbers for which we are testing cur_num presence
                    where box's row is got from row and col numbers as follows
                    box_row = row/3*3 + col/3
                    ex: for row=4, col=5, box_number 4 or check_box row number 4 is the one
                    we'll be checking
                    '''
                    if check_row[i][num] or check_col[j][num] or check_box[k][num]:
                        return False
                    #assign value to all the checking 2d arrayes
                    check_row[i][num] = check_col[j][num] = check_box[k][num] = True
        return True


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
    for row_index in xrange(0, 7, 3):
        for col_index in xrange(0, 7, 3):
            box_num = set()
            for row in xrange(row_index, row_index+3):
                for col in xrange(col_index, col_index+3):
                    num = sudoku[row][col]
                    if num == '.':
                        continue
                    if num not in box_num:
                        box_num.add(num)
                    else:
                        return 0
    return 1

if __name__ == '__main__':
    # sudoku = ["53..7....", "6..195...", ".98....6.", "8...6...3",
    #          "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
    # sudoku = ["....5..1.", ".4.3.....", ".....3..1", "8......2.","..2.7....",
    #        ".15......", ".....2...", ".2.9.....", "..4......"]
    sudoku = ["..5.....6", "....14...", ".........", ".....92..", "5....2...",
              ".......3.", "...54....", "3.....42.", "...27.6.."]

    print Solution().valid_sudoku(sudoku)
    # print valid_sudoku(sudoku)
