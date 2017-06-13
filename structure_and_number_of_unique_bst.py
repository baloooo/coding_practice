"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Idea:
https://discuss.leetcode.com/topic/8398/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i?page=1
"""


class Solution:
    def __init__(self):
        pass

    def number_of_bst(self, n):
	"""
	F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
        Time: O(n^2)
        DP Space: O(n)
	"""
	g = [0 for _ in xrange(n+1)]
	g[0] = 1
	g[1] = 1
	for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                g[i] += g[j-1] * g[n-i]
        return g[n]


if __name__ == '__main__':
    test_cases = [
        (5, 15),
    ]
    for test_case in test_cases:
        res = Solution().number_of_bst(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
