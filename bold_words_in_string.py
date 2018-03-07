'''
https://leetcode.com/articles/bold-words-in-string/
'''


class Solution:
    def __init__(self):
        pass

    def my_func(self, arg):
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
