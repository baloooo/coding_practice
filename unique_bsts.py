class Solution(object):
    def numTrees(self, n):
        """
	Time: O(n^2)
	Space: O(n)
        This to get the general idea: https://www.youtube.com/watch?v=YDf982Lb84o&t=316s
        This has the detail approach:
	https://discuss.leetcode.com/topic/8398/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i/79
        """
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in xrange(2, n+1): # This is the G(n)
            for j in xrange(1, i+1): # This is the f(n)
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    def generate_subtrees(self, start, end):
        trees = []
        for root in xrange(start, end+1):
            for left in self.generate_subtrees(start, root-1):
                for right in self.generate_subtrees(root+1, end):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees.append(node)

        return trees or [None]

    def generateTrees(self, n):
        """
	# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
	# Space: O(4^n / n^(3/2)) ~= Catalan numbers
	https://discuss.leetcode.com/topic/15886/should-be-6-liner/24
	https://discuss.leetcode.com/topic/8410/divide-and-conquer-f-i-g-i-1-g-n-i
        """
        if n == 0:
            return []
        return self.generate_subtrees(1, n)


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
