"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution:
    def __init__(self, word, grid):
        self.word = word
        self.grid = grid

    def dfs(self, cur_row, cur_col, word_index):
        if (cur_row < 0 or cur_row >= len(self.grid) or
                cur_col < 0 or cur_col >= len(self.grid[0]) or
                (cur_row, cur_col) in self.visited):
            return False
        if word_index == len(self.word):
            return True
        if self.word[word_index] == self.grid[cur_row][cur_col]:
            self.visited.add((cur_row, cur_col))
            if len(self.visited) == len(self.word):
                return True
            return(
                self.dfs(cur_row, cur_col+1, word_index+1) or
                self.dfs(cur_row, cur_col-1, word_index+1) or
                self.dfs(cur_row+1, cur_col, word_index+1) or
                self.dfs(cur_row-1, cur_col, word_index+1))
        return False

    def word_in_grid(self):
        if len(self.word) > len(self.grid)*len(self.grid[0]):
            return False
        for cur_row in xrange(len(self.grid)):
            for cur_col in xrange(len(self.grid[0])):
                if self.grid[cur_row][cur_col] == self.word[0]:
                    self.visited = set()
                    if self.dfs(cur_row, cur_col, 0):
                        return True
        return False


if __name__ == '__main__':
    # word, grid = "ABCE", [
    #       ['A', 'B', 'C', 'E'],
    #       ['S', 'F', 'C', 'S'],
    #       ['A', 'D', 'E', 'E']
    # ]
    # word, grid = "SB", [
    #       ['A'],
    #       ['S'],
    #       ['B']
    # ]
    word, grid = "ABCESEEEFS", [
        ["ABCE", "SFES", "ADEE"]
    ]
    print Solution(word, grid).word_in_grid()
