# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, target):
        if root is None: return root

        self.dfs(root.left, target)
        
        if self.found:
            if self.inorder_successor is None:
                self.inorder_successor = root
            return
        elif root == target:
            self.found = True
        self.dfs(root.right, target)
            
    def inorderSuccessor(self, root, target):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
	Time: O(n)
        """
        self.found = False
        self.inorder_successor = None
        self.dfs(root, target)
        return self.inorder_successor

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, target):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
	Time: O(h)
	https://leetcode.com/problems/inorder-successor-in-bst/discuss/72656/JavaPython-solution-O(h)-time-and-O(1)-space-iterative
	Idea:
	1. Take advantage of the fact that it is a BST and therefore can  be traversed like
	    a binary search on an array.
	2. Inorder successor is the smallest node after target node

	similar logic can be used for finding inorder predeccessors also
        """
        succ = None
        while root:
            if root.val > target.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
