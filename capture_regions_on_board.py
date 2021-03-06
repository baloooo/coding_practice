"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
surrounded by 'X'.

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
    Algo:
        a) First, check the four border of the matrix.
           If there is a 'O', alter it and all its neighbor
           'O' elements to '1'.
        b) Alter all the 'O' to 'X'
        c) At last,alter all the '1' to 'O'

    """
    def dfs(self, board, row, col):
	'''
	below bfs can be replaced by this relatively simple dfs too.
	'''
        if not(0 <= row < len(board) and 0 <= col < len(board[0])) or board[row][col] != 'O':
            return
        board[row][col] = '1'
        self.dfs(board, row+1, col)
        self.dfs(board, row-1, col)
        self.dfs(board, row, col+1)
        self.dfs(board, row, col-1)

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
                '''Notice we didn't require visited set here since we're
                modifying the cur_row, cur_col so next time around even if we
                hit it we won't pursue it since it won't satisfy the criteria
                anymore.'''
                bfs_q.put((cur_row+1, cur_col))
                bfs_q.put((cur_row-1, cur_col))
                bfs_q.put((cur_row, cur_col+1))
                bfs_q.put((cur_row, cur_col-1))

    def solve2(self, board):
        '''
        This is better than solve, since this works two border at a time.
        '''
        # check borders
        row_len = len(board)-1
        col_len = len(board[0])-1
        # North & south border
        for col in xrange(len(board[0])):
            if board[0][col] == 'O':
                # iteratively convert all 0 to 1 attached to this 0
                self.bfs(board, 0, col)
            if board[row_len][col] == '0':
                self.bfs(board, row_len, col)
        # East & West border
        for row in xrange(len(board)):
            if board[row][0] == 'O':
                self.bfs(board, row, 0)
            if board[row][col_len] == 'O':
                self.bfs(board, row, col_len)
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

################################################################################################################

    def solve(self, board):
        """
        Algo:
            a) First, check the four border of the matrix.
               If there is a 'O', alter it and all its neighbor
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

    def solve_condensed(self, board):
        if not any(board):
            return

        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]  # noqa
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]

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
        res = Solution().solve2(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
