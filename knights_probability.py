'''
[dp]
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
'''
class Solution(object):
    def possible_moves(self, r, c):
        return [
            (r+2, c+1),
            (r+2, c-1),
            (r+1, c+2),
            (r-1, c+2),
            (r+1, c-2),
            (r-1, c-2),
            (r-2, c+1),
            (r-2, c-1),
            ]

    def dfs(self, r, c, visited):
        if (r, c) in visited:
            return
        for cur_row, cur_col in self.possible_moves(r, c):
            if (cur_row, cur_col) in visited:
                continue
            else:
                visited.add((cur_row, cur_col))
            if self.total_moves == self.K:
                return
            self.total_moves += 1
            if 0 <= cur_row < self.N and 0 <= cur_col < self.N:
                self.inside_board_moves += 1
                self.dfs(cur_row, cur_col, visited)

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        Problem statement not clear: specifically how probability is calculated and how K is factored in.
        Change algo according to that and re run.
        https://leetcode.com/problems/knight-probability-in-chessboard/solution/
        https://www.geeksforgeeks.org/probability-knight-remain-chessboard/
        
        """
        self.total_moves = 0
        self.inside_board_moves = 0
        self.N, self.K = N, K
        self.dfs(r, c, set())
        import ipdb; ipdb.set_trace()
        return self.inside_board_moves/(self.total_moves*1.0)

if __name__ == '__main__':
    N, K, r, c = 3, 2, 0, 0
    print Solution().knightProbability(N, K, r, c)
