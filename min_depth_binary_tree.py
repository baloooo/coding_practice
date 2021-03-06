# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Idea: We need to add the smaller one of the child depths - except if that's zero, then add the larger one
        https://discuss.leetcode.com/topic/16869/3-lines-in-every-language
        """
        if root is None:
            return 0
        cur_depth = map(self.minDepth, [root.left, root.right])
        return 1 + (min(cur_depth) or max(cur_depth))


    def min_depth_helper(self, root):
        if root is None:
            return float('inf')
        if root.left is None and root.right is None:
            return 1
        return 1 + min(self.min_depth_helper(root.left), self.min_depth_helper(root.right))

    def min_depth_new(self, root):
        # seems same as above but was intutive.
        if root is None:
            return 0
        return self.min_depth_helper(root)