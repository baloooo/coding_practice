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


class Solution:

    def reverse(self, s):
        # https://discuss.leetcode.com/topic/58719/python-3-solutions-recursive-classic-pythonic
        r = list(s)
        i, j = 0, len(r)-1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return ''.join(r)

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])


if __name__ == '__main__':
    target_string = "the sky is blue"
    print reverse_string(target_string)
