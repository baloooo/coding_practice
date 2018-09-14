"""
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if
reverse(S) = S.

Incase of conflict, return the substring which occurs first
( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
"""


class Solution:
    def longest_palindromic_substring_optimized(target):
        # manachers algorithm, O(n)
        # https://articles.leetcode.com/longest-palindromic-substring-part-ii/
        pass

########################################################################################################################

    def max_palindrom_at_pos(self, string, i, j):
        # returns max_palindrome extending from i and j respectively
        while i >= 0 and j < len(string) and string[i] == string[j]:
            i -= 1
            j += 1
        # since loop starts at one index less than from actual start and one
        # index further down from actual end of the longest palindrome
        if self.max_len < j-i-1:
            self.start = i+1
            self.max_len = j-i-1

    def longest_palindrome_substring(self, string):
        """
        Best solution except manacher
        https://discuss.leetcode.com/topic/23498/very-simple-clean-java-solution
        Idea: https://articles.leetcode.com/longest-palindromic-substring-part-i/
        We observe that a palindrome mirrors around its center. Therefore,
        a palindrome can be expanded from its center, and there are only 2N-1 such centers.

        You might be asking why there are 2N-1 but not N centers?
        The reason is the center of a palindrome can be in between two letters.
        Such palindromes have even number of letters (such as “abba”) and its center
        are between the two ‘b’s.

        Since expanding a palindrome around its center could take O(N) time,
        the overall complexity is O(N2).
        """
        if len(string) == 0:
                return
        # Exceptions
        self.max_len = 0
        self.start = 0
        for i in xrange(len(string)):
            self.max_palindrom_at_pos(string, i, i)
            self.max_palindrom_at_pos(string, i, i+1)
        return string[self.start:self.start+self.max_len]

########################################################################################################################

    def check_palindrome(self, target):
        start = 0
        end = len(target) - 1
        while(start < end):
            if target[start] != target[end]:
                return 0
            start += 1
            end -= 1
        return 1


    def longest_palindromic_substring_naive(self, target):
        # Time complexity: O(n^3), n^2 subarrays and checking each for palindrome O(n)
        target_len = len(target)
        max_palindrome_len = 0
        max_palindrome_str = ''
        for start in xrange(target_len):
            for end in xrange(target_len, -1, -1):
                if self.check_palindrome(target[start:end]):
                    cur_palindrome_len = (end-start + 1)
                    if cur_palindrome_len > max_palindrome_len:
                        max_palindrome_len = cur_palindrome_len
                        max_palindrome_str = target[start:end]
        return max_palindrome_str

if __name__ == '__main__':
    # target = 'abccba'
    # target = "aaaabaaa"
    # target = "bananas"
    # target = "abracadabra"
    # target = "aba"
    target = "babad"
    # print longest_palindromic_substring_naive(target)
    # print longest_palindromic_substring_even_odd_palindromes(target)
    print Solution().longest_palindrome_substring(target)
