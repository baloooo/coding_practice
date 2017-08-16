# https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def has_sum(self, root, target_sum):
        if not root:
            return False
        self.cur_sum.append(root.val)
        if root.left is None and root.right is None:
            if sum(self.cur_sum) == target_sum:
                self.results.append(self.cur_sum[::])
                self.cur_sum.pop()
                return
        self.has_sum(root.left, target_sum)
        self.has_sum(root.right, target_sum)
        self.cur_sum.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.results = []
        self.cur_sum = []
        self.has_sum(root, sum)
        return self.results
