import pytest
import itertools

'''
https://leetcode.com/articles/bold-words-in-string/

Now armed with the correct mask, let's try to output the answer. A letter in position i is the first bold letter of the group if mask[i] && (i == 0 || !mask[i-1]), and is the last bold letter if mask[i] && (i == N-1 || !mask[i+1]). Alternatively, we could use itertools.groupby in Python.

Complexity Analysis

Time Complexity: create mask array (len(words) * len(each_word)) + O(len(target_str))

Space Complexity: O(N).
'''

class Solution():
    def addBoldTag_latest(self, word_list, target_str):
        """
        Todo:
        https://leetcode.com/problems/add-bold-tag-in-string/discuss/104289/c++-code-KMP+boolean-array-26ms-Hashing-+-intervals-145ms-Trie-+-boolean-array-160ms.

        Idea is to iterate over target_str and for each index see if any word from word_list starts from here.
        Change all indexes within this range in mask array to True
        Once all the start-end intervals are marked with True in mask array. Iterate over it and add all chars into
        result array until if mask[idx] is True. When that happens add a bold tag first add all chars and add a bold tag after

        Time Complexity: create mask array (len(words) * len(each_word)) * O(len(target_str))
        Space Complexity: O(N) for mask array
        """
        N = len(target_str)
        mask = [False]*N
        # Find all intervals in which words in word_list occur in target_str
        for start in xrange(N):
            for word in word_list:
                end = start+len(word)
                if target_str.startswith(word, start, end):
                    # set all indices from start to word len to True.
                    for idx in xrange(start, end):
                        mask[idx] = True
        result = [] # add individual chars initially carefully add in bold tags when necessary and lastly join and return.
        idx = 0
        # This part can make use of groupby too
        while idx < N:
            if mask[idx] is False:
                result.append(target_str[idx])
                idx += 1
            else:
                result.append('<b>')
                # Add all chars up until last True
                while idx < N and mask[idx] is True:
                    result.append(target_str[idx])
                    idx += 1

                result.append('</b>')
        return ''.join(result)

    def task(self, words, target_str):
        N = len(target_str)
        mask = [False]*len(target_str)
        '''
        Idea:
        Find start and end indexes where word is found in target_str
        since there can be overlapping strings, and can have multiple matches of the same.
        as here, where d matches at multiple places
        ((["ccb","b","d","cba","dc"], "eeaadadadc"), "eeaa<b>d</b>a<b>d</b>a<b>dc</b>"),
        '''
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
        # assert sol.task(*args) == result
        assert sol.addBoldTag(*args) == result
