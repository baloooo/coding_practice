'''
https://articles.leetcode.com/regular-expression-matching/
https://leetcode.com/articles/regular-expression-matching/
'''


class Solution:
    def __init__(self):
        pass

    def is_match_recursion(self, text, pattern):
	'''
	Time complexity: check https://leetcode.com/articles/regular-expression-matching/
	If a star is present in the pattern, it will be in the second position pattern[1].
	Then, we may ignore this part of the pattern, or delete a matching character in the text.
	If we have a match on the remaining strings after any of these operations, then the initial inputs matched.
	'''
	if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in [text[0], '.']
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or  # Take zero instances of pattern[0]
		    (first_match and self.isMatch(text[1:], pattern))) # Take one instance of pattern[0]
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def is_match_dp(self, text, pattern);
	pass

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
