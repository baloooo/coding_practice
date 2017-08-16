# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    Idea: http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
    """
    def find_max_sum(self, root):
        if root is None:
            return 0
        l = self.find_max_sum(root.left)
        r = self.find_max_sum(root.right)
        single_max = max(max(l, r)+root.val, root.val)
        max_until_now = max(single_max, l+r+root.val)
        self.max_sum = max(self.max_sum, max_until_now)
        return single_max

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = -float('inf')
        self.find_max_sum(root)
        return self.max_sum
        
