"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
class Solution(object):
    def isIsomorphic(self, base, target):
        """
        Algo:
	1) If lengths of str1 and str2 are not same, return false.
	2) Do following for every character in str1 and str2
	   a) If this character is seen first time in str1, 
	      then current of str2 must have not appeared before.
	      (i) If current character of str2 is seen, return false.
		  Mark current character of str2 as visited.
	      (ii) Store mapping of current characters.
	   b) Else check if previous occurrence of str1[i] mapped
	      to same character.
        :type s: str
        :type t: str
        :rtype: bool
        """
        # egg: add
        # abba: abab
	# aa: ab
        str_map = {}
        for base_char, target_char in zip(base, target):
            try:
                if str_map[target_char] != base_char:
                    return False
            except KeyError:
                if base_char not in str_map.values():
                    str_map[target_char] = base_char
                else:
                    return False
        return True
