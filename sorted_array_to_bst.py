# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, arr):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if arr:
            root_index = len(arr)/2
            root = TreeNode(arr[root_index])
            root.left = self.sortedArrayToBST(arr[:root_index])
            root.right = self.sortedArrayToBST(arr[root_index+1:])
            return root
