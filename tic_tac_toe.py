# https://leetcode.com/problems/design-tic-tac-toe/discuss/81898/Java-O(1)-solution-easy-to-understand?page=2
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagnol = 0
        self.anti_diagnol = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # player1: +1, player2: -1
        player_val = 1 if player == 1 else -1
        
        self.rows[row] += player_val
        self.cols[col] += player_val
    
        if row+col == (self.n - 1):
            self.anti_diagnol += player_val
        if row == col: # Note center point comes in both diagnol and anti so can't use elif here.
            self.diagnol += player_val
        
        # check if somewon won
        if (
                abs(self.rows[row]) == self.n or 
                abs(self.cols[col]) == self.n or 
                abs(self.diagnol) == self.n or 
                abs(self.anti_diagnol) == self.n):
            return player
        else:
            return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
