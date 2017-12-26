# coding: utf-8
"""
LCA for binary tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        Time: O(n) Space: O(n)
        Idea: http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
        
        Also helpful idea is that we can calculate distance b/w any two nodes by using LCA.
        Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca) 
        """
        # If either p or q is root, that's all we needed return
        if root in [p, q, None]: return root 
        left = self.lowestCommonAncestor(root.left, p, q) # search the left half
        right = self.lowestCommonAncestor(root.right, p, q) # search the right half
        # if left and half both returned vals, that would mean current root is the LCA
        if left and right:
            return root
        # Otherwise check if left subtree or right subtree is LCA
        return left if left else right

"""
LCA for Binary Search Tree
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        Idea: https://discuss.leetcode.com/topic/18614/easy-c-recursive-and-iterative-solutions
        Time: O(logn) Space: O(1)
        """
        if root is None: return
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            if root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
