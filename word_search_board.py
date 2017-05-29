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

    def dfs(self, cur_row, cur_col, word_index, path):
        """
        Added path just for more clarity to check the path taken
        by algo.
        """
        if word_index == len(self.word):
            print 'final_path is', path
            return True
        if (cur_row < 0 or cur_row >= len(self.grid) or
                cur_col < 0 or cur_col >= len(self.grid[0])):
            return False
        if self.word[word_index] == self.grid[cur_row][cur_col]:
            self.visited.add((cur_row, cur_col))
            if (cur_row, cur_col+1) not in self.visited:
                if self.dfs(cur_row, cur_col+1, word_index+1, path + [(cur_row, cur_col+1)]):  # noqa
                    return True
                """
                remove this co-ordinate from visited so that this can be used
                in some other path.
                """
                self.visited.discard((cur_row, cur_col+1))
            if (cur_row, cur_col-1) not in self.visited:
                if self.dfs(cur_row, cur_col-1, word_index+1, path + [(cur_row, cur_col-1)]):  # noqa
                    return True
                self.visited.discard((cur_row, cur_col-1))
            if (cur_row+1, cur_col) not in self.visited:
                if self.dfs(cur_row+1, cur_col, word_index+1, path + [(cur_row+1, cur_col)]):  # noqa
                    return True
                self.visited.discard((cur_row+1, cur_col))
            if (cur_row-1, cur_col) not in self.visited:
                if self.dfs(cur_row-1, cur_col, word_index+1, path + [(cur_row-1, cur_col)]):  # noqa
                    return True
                self.visited.discard((cur_row-1, cur_col))
            else:
                return False

    def exist(self):
        for cur_row in xrange(len(self.grid)):
            for cur_col in xrange(len(self.grid[0])):
                if self.grid[cur_row][cur_col] == self.word[0]:
                    self.visited = set()
                    if self.dfs(cur_row, cur_col, 0, [(cur_row, cur_col)]):
                        print self.path
                        return True
        return False

    def word_in_grid(self, grid, word_list):
        self.path = []
        self.grid = [[char for char in each] for each in grid]
        for row in self.grid:
            print row
        # if len(self.word) > len(self.grid)*len(self.grid[0]):
        #     return False
        result = []
        for word in word_list:
            self.word = word
            if self.exist():
                result.append(word)
        return result


if __name__ == '__main__':
    test_cases = [
        # ((["ABCE", "SFCS", "ADEE"], "ABCCED"), True),
        # ((["a"], "a"), True),
        # ((["aa"], "aa"), True),
        ((["ab", "cd"], ["acdb", "ca"]), ["acdb", "ca"]),
        # ((["ABCE", "SFES", "ADEE"], "ABCESEEEFS"), True),
    ]
    for test_case in test_cases:
        res = Solution().word_in_grid(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])


class Solution2:
    """
    The same letter cell may be used more than once in the grid.
    """

    def dfs(self, cur_row, cur_col, word_index, path):
        """
        Added path just for more clarity to check the path taken
        by algo.
        """
        if word_index == len(self.word):
            print 'final_path is', path
            return True
        if (cur_row < 0 or cur_row >= len(self.grid) or
                cur_col < 0 or cur_col >= len(self.grid[0])):
            return False
        if self.word[word_index] == self.grid[cur_row][cur_col]:
            # print 'path:', path
            return (
                self.dfs(cur_row, cur_col+1, word_index+1, path + [(cur_row, cur_col+1)]) or  # noqa
                self.dfs(cur_row, cur_col-1, word_index+1, path + [(cur_row, cur_col-1)]) or  # noqa
                self.dfs(cur_row+1, cur_col, word_index+1, path + [(cur_row+1, cur_col)]) or  # noqa
                self.dfs(cur_row-1, cur_col, word_index+1, path + [(cur_row-1, cur_col)]) or  # noqa
                False)

    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, grid, word):
        self.path = []
        self.grid = [[char for char in each] for each in grid]
        # for row in self.grid:
        #     print row
        self.word = word
        if len(self.word) > len(self.grid)*len(self.grid[0]):
            return 0
        for cur_row in xrange(len(self.grid)):
            for cur_col in xrange(len(self.grid[0])):
                if self.grid[cur_row][cur_col] == self.word[0]:
                    if self.dfs(cur_row, cur_col, 0, [(cur_row, cur_col)]):
                        # print self.path
                        return 1
        return 0

# if __name__ == '__main__':
#     test_cases = [
#         ((["FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA",
#            "AGFADEAC", "ADGDCBAA", "EAABDDFF"], "BCDCB"), 1),
#         ((["CDGCG", "CDAAA", "ECDDB", "FBGEC", "BEBBF", "DFGEF", "CGGAD",
#            "AACGG", "BDGGB"], "BABABC"), 1),
#         ]
#     for test_case in test_cases:
#         res = Solution2().exist(test_case[0][0], test_case[0][1])
#         if res == test_case[1]:
#             print "Passed"
#         else:
#             print "Failed: Test case: {0} Got {1} Expected {2}".format(
#                 test_case[0], res, test_case[1])
