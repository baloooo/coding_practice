"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""


class Solution:
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    https://discuss.leetcode.com/topic/18706/9-lines-python-148-ms
    """

    def __init__(self):
        pass

    def bfs(self, board, row, col):
        from Queue import Queue
        bfs_q = Queue()
        bfs_q.put((row, col))
        while not bfs_q.empty():
            cur_row, cur_col = bfs_q.get()
            if (cur_row < 0 or cur_row >= len(board) or cur_col < 0 or
                    cur_col >= len(board[0])):
                continue
            if board[cur_row][cur_col] == 'O':
                board[cur_row][cur_col] = '1'
                bfs_q.put((cur_row+1, cur_col))
                bfs_q.put((cur_row-1, cur_col))
                bfs_q.put((cur_row, cur_col+1))
                bfs_q.put((cur_row, cur_col-1))

    def solve(self, board):
        """
        Algo:
            a) First, check the four border of the matrix.
               If there is a element is 'O', alter it and all its neighbor
               'O' elements to '1'.
            b) Alter all the 'O' to 'X'
            c) At last,alter all the '1' to 'O'

        """
        # check borders
        row_len = len(board)-1
        col_len = len(board[0])-1
        # North border
        for col, ch in enumerate(board[0]):
            if ch == 'O':
                # iteratively convert all 0 to 1 attached to this 0
                self.bfs(board, 0, col)
        # East border
        for row_num, row in enumerate(board):
            if row[col_len] == 'O':
                self.bfs(board, row_num, col_len)
        # South border
        for col, ch in enumerate(board[-1]):
            if ch == 'O':
                # iteratively convert all 0 to 1 attached to this 0
                self.bfs(board, row_len, col)
        # West border
        for row_num, row in enumerate(board):
            if row[0] == 'O':
                self.bfs(board, row_num, 0)
        # Alter all '0' to 'X'
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        # Revert back all '1' to '0'
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                if board[row][col] == '1':
                    board[row][col] = 'O'
        print 'result board'
        for row in board:
            print row
        print 'expected'
        res_board = ["XXXX", "XXXX", "XXXX", "XOXX"]
        for row in res_board:
            print row
if __name__ == '__main__':
    # inp = ["XOXOXO", "OXOXOX", "XOXOXO", "OXOXOX"]
    inp = ["XXXX", "XOOX", "XXOX", "XOXX"]
    board = [[ch for ch in row] for row in inp]
    # board = [ch for ch in row for row in inp]
    for row in board:
        print row
    test_cases = [
        (board, True),
    ]
    for test_case in test_cases:
        res = Solution().solve(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
