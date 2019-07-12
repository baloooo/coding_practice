"""
Given a digit string, return all possible letter combinations that the number could represent.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

I think it is 4^n where 4 comes from the maximum amount of letters possible for a digit.

For example, the number "9" has 4 letters: "wxyz."

If the input is "9" you will get 4 results. If the input is "99" you will get 16 results, etc. At each digit, we take the previous results, and for EACH letter corresponding to the digit, we append the letter to the previous results.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        Time: O(4^n)
        chapter 7: recursion Problem Telephone words
        This requires combinatorial mathematics, but if you don’t remember this
type of math, don’t panic. First, try a one-digit phone number. Clearly, this would have three words.
Now, try a two-digit phone number — say, 56. There are three possibilities for the first letter, and for
each of these there are three possibilities for the second letter. This yields a total of nine words that
can correspond to this number. It appears that each additional digit increases the number of words by
a factor of 3. Thus, for 7 digits, you have 37 words, and for a phone number of length n, you have 3n

        Space: Used for
        Idea: https://stackoverflow.com/questions/2344496/how-can-i-print-out-all-possible-letter-combinations-a-given-phone-number-can-re
        """
        if not digits:
            return []
        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
        combinations = ['']
        for digit in digits:
            cur_str = num_map[digit]
            combinations = [prefix+suffix for prefix in combinations for suffix in cur_str]
			# above is similar to this, it just alleivates handling of temp array which
			# list comprehension takes care of.
            # temp = []
            # for prefix in combs:
            #     for suffix in cur_str:
            #         temp.append(prefix+suffix)
            # combs = temp
        return combinations

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        Time: O(n*4^n)
        Idea: Apparently this implementation would help to wrap your head around
        the time complexity for the algo
        """
        n, res = len(digits), []
        if n == 0: return res
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for i in range(n):
            num = int(digits[i])
            temp = []
            for c in letters[num]:
                if len(res) == 0:
                    temp.append(c)
                else:
                    for j in range(len(res)):
                        temp.append(res[j]+c)
            res[:] = temp
        return res


    def letterCombinations(self, digits):
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']
        for digit in digits:
            res = [prefix + suffix for prefix in res for suffix in letters[digit]]

        return res

