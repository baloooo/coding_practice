"""
    Analysis, explanation: https://leetcode.com/problems/longest-common-prefix/solution/
    Example:
    Given the array as:
    [
      "abcdefgh",

      "aefghijk",

      "abcefgh"
    ]
    ans: a
"""

class TrieNode(object):
    def __init__(self, char):
        self.child_map = {}
        self.end_of_word = False


class TrieSolution():
    def lcp_by_trie(str_list):
        '''
        If lcp needs to called multiple times for a given string, use trie.
        Time complexity : preprocessing O(S), where SS is the number of all characters in the array, LCP query O(m).

        Trie build has O(S) time complexity. To find the common prefix of qq in the Trie takes in the worst case O(m).

        Space complexity : O(S). We only used additional SS extra space for the Trie.
        '''
        main_root = root = TrieNode()
        # add strings to trie
        for cur_str in str_list:
            for cur_char in cur_str:
                if cur_char not in root.child_map:
                    node = TrieNode()
                    root.child_map[cur_char] = node
            root.end_of_word = True
            root = main_root
        # find lcp in trie
        # print trie_obj.trie

class Solution(object):
    def word_by_word(str_list):
        """
        Recommended solution: Vertical scan
        n = #f strings
        m = length of smallest string
        Time: O(n*m)
        """
        if not strs: return ""
        min_len_str = strs[0]
        for i in xrange(1, len(strs)):  # find min len string
            if len(strs[i]) < len(min_len_str):
                min_len_str = strs[i]

        for word in strs:
            for i in xrange(len(min_len_str)):
                if word[i] != min_len_str[i]:
                    min_len_str = word[:i]
                    break
            if not min_len_str: # if at any time min_len_str is null, no need to go ahead.
                break
        return min_len_str

    def lcp(self, str1, str2):
        for i in xrange(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return str1[:i]
        # Execution reached here would suggest both strings are equal untill the length of min. string.
        if len(str1) < len(str2):
              return str1
        else:
              return str2

    def longestCommonPrefix(self, strs):
        """
        horizontal scanning: Here we'll scan every word of the list entirely to get our result.
        A minor optimization can be to either stop when lcp got to zero or up to the length
        of min len word in the list since we can't go below or above these limits.
        Overall making a vertical scan is better than horizontal scan since you will never
        go over the min length word with a vertical scan even when you have a million char
        word in your list, whereas in horizontal you can.
        Though their asymptotic time complexities are same
        """
        #if any([not (len(s)) for s in strs]):
        #    return ''
        if strs:
            res = reduce(self.lcp, strs)
            # since if empty string array is passed reduce returns None
            if res is None: return ''
            else: return res
        else:
            return ''
        

if __name__ == '__main__':
    strs = ["a", "a", "b"]
    strs = ["a", "c", "b"]
    strs = ["", "", ""]
    strs = ["a"]
    strs = [""]
    print Solution().longestCommonPrefix(strs)
    # str_list = ["abcdefgh", "aefghijk", "abcefgh"]
    # str_list = ["geek", "gee", "geeks"]
    # print "result by word_by_word", word_by_word(str_list)
    # print "result by lcp", lcp_by_trie(str_list)
