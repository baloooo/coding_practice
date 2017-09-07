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
        self.children = defaultdict(TrieNode())
        self.is_word = False


class Solution:
    def create_trie(self, word_list):
        root = TrieNode()
        for word in word_list:
            cur_root = root
            for char in word:
                cur_root = cur_root.children[char]
        return root

    def dfs(self, root):
        if root is None:
            return
        if root.is_word:
            return root


    def find_word_w_prefix(self, root, prefix):
        for i in xrange(len(prefix)):
            root = root.children[prefix[i]]
        # either store all prefixes on node
        # return root.prefixes
        # run DFS from here to find all prefixes
        self.dfs(root)

    def find_word_square(self, word_list):
        """
        https://discuss.leetcode.com/topic/63428/short-python-c-solution
        https://discuss.leetcode.com/topic/63516/explained-my-java-solution-using-trie-126ms-16-16
        """
        root = self.create_trie(word_list)
        # Iterate over words and search for matching prefix
        final_word_lists = []
        for cur_index in xrange(len(word_list)):
            word_list[cur_index], word_list[0] = word_list[0], word_list[cur_index]  # noqa
            possible_word_arrngmnt = [word_list[0]]
            # this assumes atleast 2 char
            cur_prefix = [word_list[0][1]]
            for index in xrange(1, len(word_list[0])):
                next_word = self.find_word_w_prefix(root, cur_prefix)
                possible_word_arrngmnt.append(next_word)
                cur_prefix.append(possible_word_arrngmnt[index][len(possible_word_arrngmnt)])  # noqa
            word_list[cur_index], word_list[0] = word_list[0], word_list[cur_index]  # noqa
        return final_word_lists

if __name__ == '__main__':
    test_cases = [
        (["area", "lead", "wall", "lady", "ball"], 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
