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
        if not board:return False
        for row in board:
            for ele in row:
                print ele,
            print
        m,n=len(board),len(board[0])
        check_row=[[0 for i in range(9)] for j in range(9)]#three 2d array to check each row, col and sub box
        check_col=[[0 for i in range(9)] for j in range(9)]#three 2d array to check each row, col and sub box
        check_box=[[0 for i in range(9)] for j in range(9)]#three 2d array to check each row, col and sub box
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] != '.':
                    num=int(board[i][j])-1 # need -1 becasue the index of array is 0~8
                    k=i/3*3+j/3
                    import ipdb; ipdb.set_trace()
                    #because if previously the same number of same row,col or box have exist, it is false
                    if check_row[i][num] or check_col[j][num] or check_box[k][num]:
                        return False
                    #assign value to all the checking 2d arrayes
    
                    check_row[i][num]=check_col[j][num]= check_box[k][num]=1
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
