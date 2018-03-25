'''
https://leetcode.com/problems/add-bold-tag-in-string/solution/
can also be done using the combination of dict and merge interval techiniqe
https://leetcode.com/problems/add-bold-tag-in-string/discuss/104289/c++-code-KMP+boolean-array-26ms-Hashing-+-intervals-145ms-Trie-+-boolean-array-160ms.
'''

class Solution:

    def my_func(self, t_s, words):
        '''
        using mask array
        if s.size() = m, dict.size() = k, longest word length in dict is n.
        time: m*(n+k), As for each index in t_s(m), we can at max go to all k
        or one k all along till its lenght n

        Solution().boldWords("aaabbcc", ["aaa", "aab", "bc"])
        Prefix: aaabbcc, word: aaa, i: 0
        Prefix: aabbcc, word: aab, i: 1
        Prefix: bcc, word: bc, i: 4
        mask: [True, True, True, True, True, True, False]
        Out[18]: '<b>aaabbc</b>c'
        '''
        if not t_s: return ''
        if not words: return t_s
        words = set(words)
        mask = [False]*len(t_s)
        for i in xrange(len(t_s)):
            prefix = t_s[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in xrange(i, min(i+len(word), len(t_s))):
                        mask[j] = True
        res = []
        open_braces = close_braces = False
        i = 0
        while i < len(t_s):
            if mask[i] is True and open_braces is False:
                res.append('<b>')
                open_braces = True
                close_braces = True
            elif mask[i] is False and close_braces is True:
                res.append('</b>')
                open_braces = False
                close_braces = False
            res.append(t_s[i])
            i += 1
        if close_braces: # If string is at the last part and close brace is still true
            res.append('</b>')
        return ''.join(res)

if __name__ == '__main__':
    test_cases = [
        (("aaabbcc", ["aaa", "aab", "bc"]), '<b>aaabbc</b>c'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0][0], res, test_case[1])
