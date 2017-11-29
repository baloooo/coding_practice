'''
https://discuss.leetcode.com/topic/99281/o-log-n-java-1-line-o-log-n-k-ruby/13
https://leetcode.com/articles/find-k-closest-elements/
'''


class Solution:
    def k_closest(self, arr):
        lo, hi = 0, len(arr)-1
        while lo < hi:
            mid = lo + (hi-lo)/2


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
