# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        Idea: https://discuss.leetcode.com/topic/21287/python-short-recursive-solution/12
        """
        if inorder:
            cur_root_index = inorder.index(preorder.pop(0))
            cur_root = TreeNode(inorder[cur_root_index])
            cur_root.left = self.buildTree(preorder, inorder[:cur_root_index])
            cur_root.right = self.buildTree(preorder, inorder[cur_root_index+1:])
            return cur_root
