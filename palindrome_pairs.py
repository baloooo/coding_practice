'''
one possible solution: https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation

Using Trie: https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n*k2)-java-solution-with-Trie-structure

'''
import pytest

class Solution():
    def is_palindrome(self, word):
            return word == word[::-1]

    def palindrome_pairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        Time: O((k^2) * n), where k is the length of each word and there're total n words
        """
        palindromes = []
        words = {word: i for i, word in enumerate(words)}

        for word, k in words.items():
            for j in xrange(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                if self.is_palindrome(prefix):
                    back = suffix[::-1] # Note: We check reverse of suffix when prefix is a palindrome and vice-versa.
                    if back != word and back in words:
                        palindromes.append([words[back], k])
                if j != len(word) and self.is_palindrome(suffix):
                    back = prefix[::-1]
                    if back!= word and back in words:
                        palindromes.append([k, words[back]])
        return palindromes

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        (['bat', 'tab', 'cat'], [[0, 1], [1, 0]]),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.palindrome_pairs(args) == result
