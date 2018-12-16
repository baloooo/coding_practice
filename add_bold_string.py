'''
https://leetcode.com/problems/add-bold-tag-in-string/solution/
can also be done using the combination of dict and merge interval technique
https://leetcode.com/problems/add-bold-tag-in-string/discuss/104289/c++-code-KMP+boolean-array-26ms-Hashing-+-intervals-145ms-Trie-+-boolean-array-160ms.
As can be seen in all the solutions provided in the link above, which solution to use largely depends
on the sizes of m, k and n. some solutions are good for small k, some for small m and so on.
'''
import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur_root = self.root
        for ch in word:
            cur_root = cur_root.children[ch]
        cur_root.is_word = True

    def search(self, word, start):
        cur_root = self.root
        idx = start
        while idx < len(word):
            if word[idx] in cur_root.children:
                cur_root = cur_root.children[word[idx]]
            else:
                break
            idx += 1
        return idx if cur_root.is_word else -1


class Solution:

    def bold_trie(self, s, word_list):
        '''
        add bold to strings using Trie data structure.
        Idea is to use trie to store all words in the word_list/dict and then for each substring of "s" find
        the longest prefix in Trie. Use the longest prefix found to mask the bold boolean array.
        Finally use bold array to bold the target string similar to all the other methods like bruteforce.

        k = size of word_list
        m = target string size (s)
        n = length of largest string in word_list.

        Time: O(kn + mn), where kn for constructing trie, mn for finding all substrings of s in trie up to length n.
        Space: kn for the trie.
        '''
        word_max_len = 0
        trie = Trie()
        # create trie
        for word in word_list:
            trie.add(word)
            word_max_len = max(word_max_len, len(word))
        bold_intervals = [False]*len(s) # boolean array for creating intervals
        # search each substring of s in trie
        for start in xrange(len(s)):
            #for end in xrange(start, min(start+word_max_len, len(s))):
            end_ptr = trie.search(s, start) # returns the end index till where string is found.

            # set True on bold_intervals array from start to end_ptr
            for idx in xrange(start, end_ptr):
                bold_intervals[idx] = True

        # add bold tags in string.
        bolded_string = []
        bold_flag = False
        for idx in xrange(len(bold_intervals)):
            if bold_intervals[idx] is True:
                if bold_flag is False:
                    bolded_string.append('<b>')
                    bold_flag = True
            elif bold_flag is True:
                bolded_string.append('</b>')
                bold_flag = False

            bolded_string.append(s[idx])
        if bold_flag is True:
            bolded_string.append('</b>')

        return ''.join(bolded_string)


    def bold_bruteforce(self, t_s, words):
        '''
        using mask array
        if s.size() = N, dict.size() = d, longest word length in dict is k.
        time: N * sum_of(wi), where wi is d*k
        As for each character in N, we will go over all the words in dict to find a match with this char and go all the way up to length k.

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
        (("abcdef", ["ab", "bc", "cd", "de", "ef", "fg", "gh"]), '<b>abcdef</b>')
    ]
    for test_case in test_cases:
        # res = Solution().my_func(test_case[0][0], test_case[0][1])
        res = Solution().bold_trie(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0][0], res, test_case[1])
