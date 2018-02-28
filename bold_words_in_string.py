import pytest
import itertools

'''
https://leetcode.com/articles/bold-words-in-string/

Now armed with the correct mask, let's try to output the answer. A letter in position i is the first bold letter of the group if mask[i] && (i == 0 || !mask[i-1]), and is the last bold letter if mask[i] && (i == N-1 || !mask[i+1]). Alternatively, we could use itertools.groupby in Python.

Complexity Analysis

Time Complexity: create mask array(len(words) * len(each_word)) + O(len(target_str))

Space Complexity: O(N).
'''

class Solution():
    def task(self, words, target_str):
        N = len(target_str)
        mask = [False]*len(target_str)
        # Find start and end indexes where word is found in target_str
        # since there can be overlapping strings, and can have multiple matches of the same.
        # as here, where d matches at multiple places
        # ((["ccb","b","d","cba","dc"], "eeaadadadc"), "eeaa<b>d</b>a<b>d</b>a<b>dc</b>"),
        for i in xrange(N):
            prefix = target_str[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in xrange(i, min(i+len(word), N)):
                        mask[j] = True
        res = []
        for include, string in itertools.groupby(zip(mask, target_str), lambda x: x[0]):
            if include:
                res.append('<b>')
            for ch in string:
                res.append(ch[1]) # since we're zipping ch is (True, 'b') sort of tuple
            if include:
                res.append('</b>')
        return ''.join(res)

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        ((['ab', 'bc'], 'aabcd'), 'a<b>abc</b>d'),
        ((['ab', 'bc'], 'xyzw'), 'xyzw'),
        (([], 'xyzw'), 'xyzw'),
        ((['ab', 'bc'], ''), ''),
        (([], ''), ''),
        ((["ccb","b","d","cba","dc"], "eeaadadadc"), "eeaa<b>d</b>a<b>d</b>a<b>dc</b>"),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.task(*args) == result
