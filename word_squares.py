# coding: utf-8
"""
Given a set of words (without duplicates), find all word squares you can build
from them.

A sequence of words forms a valid word square if the kth row and column read
the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word
square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:

There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
"""


from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Solution:
    """
    Todo: compltete todo for below input (possibly using recursion)
    https://github.com/kamyu104/LeetCode/blob/master/Python/word-squares.py
    https://discuss.leetcode.com/topic/66636/python-understandable-solution-i-guess/2
    """
    def create_trie(self, word_list):
        root = TrieNode()
        for word in word_list:
            cur_root = root
            for char in word:
                cur_root = cur_root.children[char]
            cur_root.is_word = True
        return root

    def dfs(self, root, prefix):
        if root is None:
            return
        if root.is_word:
            self.prefixes.append(prefix[:])
        for key, child in root.children.items():
            self.dfs(child, prefix+[key])

    def search_prefix(self, root, prefix):
        for i in xrange(len(prefix)):
            root = root.children[prefix[i]]
        # either store all prefixes on node
        # return root.prefixes
        # run DFS from here to find all prefixes
        self.prefixes = []
        self.dfs(root, prefix)
        return self.prefixes

    def build(self, square):
        if len(square) >= self.n:
            # since once length of square gets equal to n we can't get a match
            # so fold and go home, we've found a match since we were returning only
            # matching prefixes
            self.squares.append(square)
            return
        cur_prefix = [each[len(square)] for each in square]
        for word in self.search_prefix(self.root, cur_prefix):
            self.build(square + [word])

    def find_word_square(self, word_list):
        """
        https://discuss.leetcode.com/topic/63428/short-python-c-solution
        https://discuss.leetcode.com/topic/63516/explained-my-java-solution-using-trie-126ms-16-16
        """
        self.n = len(word_list)
        self.root = self.create_trie(word_list)
        # Iterate over words and search for matching prefix
        self.squares = []
        for word in word_list:
            self.build([list(word)])
        return self.squares

if __name__ == '__main__':
    test_cases = [
        # (["area", "lead", "wall", "lady"], 'sol1'),
        # (["area", "lead", "wall", "lady", "ball"], 'sol1'),
        (["abat", "baba", "atan", "atal"], 'sol1'),
        # (["aaa", "aaa", "aaa", "aaa", "aaa"], 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().find_word_square(test_case[0])
        print 'Result ', res
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
