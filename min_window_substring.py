# coding: utf-8
import collections
'''
Minimum window in S that contains T
Method 1 ( Brute force solution )
1- Generate all substrings of string1 (“this is a test string”)
2- For each substring, check whether the substring contains all characters of string2 (“tist”)
3- Finally, print the smallest substring containing all characters of string2.
O(m*(n^2)) where m is the length of T and n length of S.
'''


class Solution:
    '''
    1. Use two pointers: start and end to represent a window.
    2. Move end to find a valid window.
    3. When a valid window is found, move start to find a smaller window.
    '''
    def minWindow(self, s, t):
        """
        Idea: http://articles.leetcode.com/finding-minimum-window-in-s-which/
            https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems/76
        s: base string
        t: target
        need_to_find is a map of characters in target to their frequency
        Time: 
        Space: 
        """
        if not s or not t or len(s) < len(t):
            return ''
        need_to_find, have_found = collections.defaultdict(int), collections.defaultdict(int)
        min_window_len, min_window_start = float('inf'), 0
        start, end, count = 0, 0, 0  # count keeps track of already matched chars of T
        for c in t:
            need_to_find[c] += 1
        #while end < len(s):
        for end in xrange(len(s)):
            # skip characters not in T
            if s[end] not in need_to_find:
                #end += 1
                continue
            have_found[s[end]] += 1  # register that we encountered s[end]
            if have_found[s[end]] <= need_to_find[s[end]]:
            # Notice need_to_find can have useless chars with zero value
                count += 1
            if count == len(t):
                # if window found, try finding a smaller window.
                # Advance start index as far right as possible,
                # stop when advancing breaks window constraint.
                while have_found[s[start]] > need_to_find[s[start]] or need_to_find[s[start]] == 0:
                    if have_found[s[start]] > need_to_find[s[start]]:
                        have_found[s[start]] -= 1
                    start += 1
                # Update min_window if shorter length is met.
                cur_win_len = end - start + 1
                if cur_win_len < min_window_len:
                    min_window_len = cur_win_len
                    min_window_start = start
        return s[min_window_start:min_window_start+min_window_len] if min_window_len != float('inf') else ''


if __name__ == '__main__':
    test_cases = [
        # (('ab', "b"), 'b'),
        (('bdab', "ab"), 'ab'),
    ]
    for test_case in test_cases:
        res = Solution().minWindow(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
