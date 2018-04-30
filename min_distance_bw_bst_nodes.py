# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def dfs(self, root):
        if root is None: return
        
        self.dfs(root.left)
        
        self.min_diff = min(self.min_diff, abs(root.val - self.prev))
        self.prev = root.val
        
        self.dfs(root.right)
    
    def minDiffInBST(self, root):
        """
	https://leetcode.com/problems/minimum-distance-between-bst-nodes/solution/
	Idea is to do an inorder traversal maintaining prev and min_differnce.
        """
        self.min_diff = float('inf')
        self.prev = float('inf')
        self.dfs(root)
        return self.min_diff
