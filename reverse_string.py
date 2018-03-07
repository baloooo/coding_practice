"""
Problem statement:

    Given an input string, reverse the string word by word.

    Example:

    Given s = "the sky is blue",

    return "blue is sky the".

	    A sequence of non-space characters constitutes a word.
	    Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
	    If there are multiple spaces between words, reduce them to a single space in the reversed string.
"""


import pytest


class Solution:
    def custom_reverse(self, arr, i, j):
        '''
        custom reverse method that reverses arr elements [i, j]
        '''
        while 0 <= i < j < len(arr):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def reverseWords_without_extra_space(self, str_list):
        """
        https://leetcode.com/problems/reverse-words-in-a-string/discuss/47740/In-place-simple-solution
        Time: O(n), Space: O(1)
        Deals with multiple starting, and trailing spaces
        Steps:
        """
        self.custom_reverse(str_list, 0, len(str_list)-1)
        store_index = i = 0
        while i < len(str_list):
            if str_list[i] != ' ':
                j = i
                if store_index != 0:
                    str_list[store_index] = ' '
                    store_index += 1
                while j < len(str_list) and str_list[j] != ' ':
                    str_list[store_index] = str_list[j]
                    store_index += 1
                    j += 1
                self.custom_reverse(str_list, i, store_index-1)
                i = j
            else:
                i += 1
        # Blank out remaining part of the array
        for index in xrange(store_index+1, len(str_list)):
            str_list[index] = ' '

    def reverse_entire_string(self, s):
        '''
        Reverses entire string without taking in account spaces, or anything else.
        https://discuss.leetcode.com/topic/58719/python-3-solutions-recursive-classic-pythonic
        '''
        # As strings are immutable in python we should be provided a string in
        # list form, so this shouldn't be necessary
        r = list(s)
        i, j = 0, len(r)-1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return ''.join(r)


class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        (["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"],
         ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]),
        ])
    def test_task(self, args, result):
        sol = Solution()
        sol.reverseWords_without_extra_space(args) 
        assert args== result
