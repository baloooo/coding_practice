"""
Given a digit string, return all possible letter combinations that the number could represent.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
	Idea: https://stackoverflow.com/questions/2344496/how-can-i-print-out-all-possible-letter-combinations-a-given-phone-number-can-re
        """
        if not digits:
            return []
        num_map = {"2": "abc","3": "def","4": "ghi","5": "jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        combinations = ['']
        for digit in digits:
            cur_str = num_map[digit]
            combinations = [prefix+suffix for prefix in combinations for suffix in cur_str]
        return combinations
