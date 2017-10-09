# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if self.pre and self.pre.val > root.val:
            # Notice: the first time an anomaly is encountered our target is in first node self.pre, whereas for the
            # second node our target will be in latter node therefore in root
            if self.first is None:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inorder(root.right)
            
    def recoverTree(self, root):
        """
	Time: O(n) Space: O(h) stack space
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
	Idea: https://discuss.leetcode.com/topic/3988/no-fancy-algorithm-just-simple-and-powerful-in-order-traversal/63
        """
        self.first = self.second = self.pre = None
        self.inorder(root)
        if self.first is not None:
            self.first.val, self.second.val = self.second.val, self.first.val
