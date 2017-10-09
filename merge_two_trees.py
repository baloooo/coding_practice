# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
	Idea: https://discuss.leetcode.com/topic/92214/python-straightforward-with-explanation
        """
        if t1 is None and t2 is None: return
	# Note: These enclosing braces are not optional
        root = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        root.left = self.mergeTrees(t1.left if t1 and t1.left else None, t2.left if t2 and t2.left else None)
        root.right = self.mergeTrees(t1.right if t1 and t1.right else None, t2.right if t2 and t2.right else None)
        return root
