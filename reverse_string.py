"""
All are O(n) and O(1) space
"""


import pytest


class Solution:
    def custom_reverse(self, str_list, start, end):
        '''
        custom reverse method that reverses arr elements [i, j]
        '''
        while start < end:
            str_list[start], str_list[end] = str_list[end], str_list[start]
            start += 1
            end -= 1
        
            
    def reverseWords_wo_spaces(self, str_list):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        reverse words in a string 2
        Assumes there're no leading or trailing spaces, and there is only
        one space between words.
        We can loop once over str_list if these conditions are not guaranteed.
        """
        i = 0
        self.custom_reverse(str_list, 0, len(str_list)-1)
        while i < len(str_list):
            start = i
            while i < len(str_list) and str_list[i] != ' ':
                i += 1
            self.custom_reverse(str_list, start, i-1)
            i += 1

########################################################################################################
    def sanitize(self, str_list):    
        i, j = 0, 0
        while j < len(str_list):
            while j < len(str_list) and str_list[j] == ' ': j+= 1
            while j < len(str_list) and str_list[j]!= ' ':
                str_list[i] = str_list[j]
                i += 1
                j += 1
            while j < len(str_list) and str_list[j] == ' ': j+=1
            if j < len(str_list):
                str_list[i] = ' ' 
                i += 1
        return i-1

    def reverseWords_w_spaces(self, s):
        """
        reverse_words when there can be multiple spaces at start, beginning or in middle.
        :type str: str
        :rtype: str
        https://leetcode.com/problems/reverse-words-in-a-string/discuss/47720/Clean-Java-two-pointers-solution-(no-trim(-)-no-split(-)-no-StringBuilder)
        """
	# LCode gave this as string but in python strings are immtable so have to be
	# changed in problem statement. Except for this it's O(n) time and O(1) space
        str_list = list(s)
        i = 0
        new_str_list_len = self.sanitize(str_list)
        if new_str_list_len == -1: return ""
        self.custom_reverse(str_list, 0, new_str_list_len)
        while i <= new_str_list_len:
            start = i
            while i <= new_str_list_len and str_list[i] != ' ':
                i += 1
            self.custom_reverse(str_list, start, i-1)
            i += 1
        return ''.join(str_list[:i-1])
########################################################################################################

    def custom_reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords_w_spaces(self, s):
        """
		Seems better than using sanitize method
        """
        s = list(s)
        self.custom_reverse(s, 0, len(s)-1)
        base, start, end = 0, 0, 0
        while end < len(s):
            if s[end] != ' ':
                start = end 
                while end < len(s) and s[end] != ' ':
                    end += 1
                self.custom_reverse(s, start, end-1)
                if base != 0:  # For adding one space before every word(except first)
                    s[base] = ' '
                    base += 1
                while start < end: # copy reversed list over to correct spot, delimetered by base
                    s[base] = start
                    base += 1
                    start += 1
                
            else:
                end += 1

        return ''.join(s[:base])


class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        # (["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"],
        #  ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]),
	("   the   sky is    blue    ", "blue is sky the"),
	(" ", ""),
	("    ", ""),
	("a", "a"),
	(" a", "a"),
	("a ", "a"),
	(" a ", "a"),
        ])
    def test_task(self, args, result):
        sol = Solution()
        # sol.reverseWords_without_extra_space(args) 
	retrned_op = sol.reverseWords(args)
        assert retrned_op == result
