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
class Solution(object):
    '''
    This is the latest solution
    Time: (m*n*(4^L)) m*n is the dimension of board and for each char in the board we dfs, which
    has TC 4^L as at each step in DFS, we have max 4 choices and there are at max L steps where L is the 
    number of words in word to be searched
    https://discuss.leetcode.com/topic/37162/what-is-the-time-complexity-for-the-dfs-solution/11
    Note: I think we should just use trie as in word_search_board2 as it's time complexity is m*n*L if space
    is not an issue, as trie takes O(L*p) space where p is the size of each word and L #f words
    '''
    def dfs(self, board, row, col, word, index, visited):
        if index == len(word): return True
        if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or 
                board[row][col] != word[index] or (row,col) in visited):
            return False
        visited.add((row, col))
        exist = (
            self.dfs(board, row+1, col, word, index+1, visited) or 
            self.dfs(board, row, col+1, word, index+1, visited) or 
            self.dfs(board, row-1, col, word, index+1, visited) or 
            self.dfs(board, row, col-1, word, index+1, visited))
        visited.discard((row, col))
        return exist

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                visited = set()
                if self.dfs(board, i, j, word, 0, visited):
                    return True
        return False


class Solution(object):
    def dfs(self, board, word, index, row, col):
        if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] == '.'
                or board[row][col] != word[index]):
            return
        board[row][col] = '.'
        if index == len(word)-1:
            return True
        elif (self.dfs(board, word, index+1, row+1, col) or
                self.dfs(board, word, index+1, row, col+1) or 
                self.dfs(board, word, index+1, row-1, col) or
                self.dfs(board, word, index+1, row, col-1)):
            return True
        else:
            board[row][col] = word[index]
    
    def exist(self, board, word):
        """
	If allowed to modify the board, we can use this implementation also.
	Idea is same as above
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False
        


class Solution:
    def dfs_optimized(self, board, row, col, word, visited, word_index):
        if word_index == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        if word[word_index] != board[row][col]:
            return False
        # board[row][col] = '#' # can use this, if modifying board is allowed or visited set
        visited.add((row, col))
        exits = (
            self.dfs(board, row+1, col, word, visited, word_index+1) or
            self.dfs(board, row-1, col, word, visited, word_index+1) or
            self.dfs(board, row, col+1, word, visited, word_index+1) or 
            self.dfs(board, row, col-1, word, visited, word_index+1))
        visited.discard((row, col))
        return exist


    def exist_optimized(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                if word[0] == board[row][col]:
                    if self.dfs(board, row, col, word, set(), 0):
                        return True
        return False

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


# if __name__ == '__main__':
#     test_cases = [
#         # ((["ABCE", "SFCS", "ADEE"], "ABCCED"), True),
#         # ((["a"], "a"), True),
#         # ((["aa"], "aa"), True),
#         ((["ab", "cd"], ["acdb", "ca"]), ["acdb", "ca"]),
#         # ((["ABCE", "SFES", "ADEE"], "ABCESEEEFS"), True),
#     ]
#     for test_case in test_cases:
#         res = Solution().word_in_grid(test_case[0][0], test_case[0][1])
#         if res == test_case[1]:
#             print "Passed"
#         else:
#             print "Failed: Test case: {0} Got {1} Expected {2}".format(
#                 test_case[0], res, test_case[1])


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
class Solution3(object):
    def dfs(self, board, row, col, word, index, visited):
        if index == len(word): return True
        if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or 
                board[row][col] != word[index] or (row,col) in visited):
            return False
        visited.add((row, col))
        return (
            self.dfs(board, row+1, col, word, index+1, visited) or 
            self.dfs(board, row, col+1, word, index+1, visited) or 
            self.dfs(board, row-1, col, word, index+1, visited) or 
            self.dfs(board, row, col-1, word, index+1, visited))

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
	Todo: This didn't pass all test cases last time around.
        Time: (m*n*(4^L)) m*n is the dimension of board and for each char in the board we dfs, which
        has TC 4^L as at each step in DFS, we have max 4 choices and there are at max L steps where L is the 
        number of words in word to be searched
        https://discuss.leetcode.com/topic/37162/what-is-the-time-complexity-for-the-dfs-solution/11
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                visited = set()
                if self.dfs(board, i, j, word, 0, visited):
                    return True
        return False
                
if __name__ == '__main__':
    test_cases = [
#         ((["FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA",
#            "AGFADEAC", "ADGDCBAA", "EAABDDFF"], "BCDCB"), 1),
#         ((["CDGCG", "CDAAA", "ECDDB", "FBGEC", "BEBBF", "DFGEF", "CGGAD",
#            "AACGG", "BDGGB"], "BABABC"), 1),
	  (([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"), True)
        ]
    for test_case in test_cases:
        # res = Solution2().exist(test_case[0][0], test_case[0][1])
        res = Solution3().exist(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
