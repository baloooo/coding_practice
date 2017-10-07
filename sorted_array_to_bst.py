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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_bst(self, arr, start, end):
        if start > end:
            return None
        mid = start + (end-start)/2
        root = TreeNode(arr[mid])
        root.left = self.get_bst(arr, start, mid-1)
        root.right = self.get_bst(arr, mid+1, end)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        Idea: http://articles.leetcode.com/convert-sorted-array-into-balanced/
        This one is more standard
        """
        if not nums: return
        return self.get_bst(nums, 0, len(nums)-1)
