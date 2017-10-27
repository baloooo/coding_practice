# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorder(self, root, min_arr):
        if root is None: return
        if root.val < min_arr[0]:
            min_arr[0], min_arr[1] = root.val, min_arr[0]
        elif root.val < min_arr[1] and root.val != min_arr[0]:
            min_arr[1]  = root.val
        self.preorder(root.left, min_arr)
        self.preorder(root.right, min_arr)

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_arr = [float('inf'), float('inf')]
        self.preorder(root, min_arr)
        return -1 if min_arr[-1] == float('inf') else min_arr[-1]
