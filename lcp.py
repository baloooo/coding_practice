"""
    Write a function to find the longest common prefix string amongst an array
    of strings.

    Longest common prefix for a pair of strings S1 and S2 is the longest
    string S which is the prefix of both S1 and S2.

    As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

    Given the array of strings, you need to find the longest S which is the
    prefix of ALL the strings in the array.

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


def lcp_by_trie(str_list):
    main_root = root = TrieNode()
    # add strings to trie
    for cur_str in str_list:
        for cur_char in cur_str:
            if cur_char not in root.child_map:
                node = TrieNode()
                root.child_map[cur_char] = node
        root.end_of_worda = True
        root = main_root
    # find lcp in trie
    # print trie_obj.trie


def word_by_word(str_list):
    """
    n = #f strings
    m = length of smallest string
    O(n*m)
    """
    min_len_string = str_list[0]
    min_len_string_len = len(str_list[0])
    for string in str_list[1:]:
        if len(string) < min_len_string_len:
            min_len_string = string
            min_len_string_len = len(string)
    for string in str_list:
        for index, char in enumerate(min_len_string):
            if char != string[index]:
                min_len_string = string[:index]
                break
    return min_len_string

if __name__ == '__main__':
    # str_list = ["abcdefgh", "aefghijk", "abcefgh"]
    str_list = ["geek", "gee", "geeks"]
    # print "result by word_by_word", word_by_word(str_list)
    print "result by lcp", lcp_by_trie(str_list)

"""
LCP for strings
"""
class Solution(object):
    def lcp(self, str1, str2):
        index = 0
        for index in xrange(min(len(str1), len(str2))):
            if str1[index] == str2[index]:
                index += 1
            else:
                break
        return str1[:index]
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            return reduce(self.lcp, strs)
        else:
            return ''
