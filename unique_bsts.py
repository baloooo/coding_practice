class Solution(object):
    def numTrees(self, n):
        """
	Time: O(n^2)
	Space: O(n)
	https://discuss.leetcode.com/topic/8398/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i/79
	https://www.youtube.com/watch?v=YDf982Lb84o&t=316s
        """
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

    def generate_subtrees(self, start, end):
        if (start, end) in self.dp:
            return self.dp[(start, end)]
        if start > end:
            return [None]

        trees = []
        for root_idx in xrange(start, end+1):
            left_subtrees = self.generate_subtrees(start, root_idx-1)
            right_subtrees = self.generate_subtrees(root_idx+1, end)

            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root = TreeNode(root_idx)
                    root.left = left_subtree
                    root.right = right_subtree
                    trees.append(root)

        self.dp[(start, end)] = trees
        return trees

    def generateTrees_optimized(self, n):
        """
		# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
		# Space: O(4^n / n^(3/2)) ~= Catalan numbers
		https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31508/Divide-and-conquer.-F(i)-G(i-1)-*-G(n-i)
		This implementation is more inline with numTrees implementation, therefore more intutive
		Also this implementation caches subtrees which improves performance
        """
        if n == 0: return []
        self.dp = {}
        return self.generate_subtrees(1, n)

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
