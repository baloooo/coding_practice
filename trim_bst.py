# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        Idea: https://discuss.leetcode.com/topic/102034/java-solution-6-liner/18
        """
        if root is None: return None
        # root is out of range, so skip root and everything left of it since everything left
        # of root will also be surely less than root
        if root.val < L: return self.trimBST(root.right, L, R)
        # same as above, if root is greater than R everything on root.right will also be.
        if root.val > R: return self.trimBST(root.left, L, R)
        # if root is in range recursively test their children
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
