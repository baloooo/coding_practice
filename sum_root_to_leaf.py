class Solution(object):
    def total_sum(self, root, sum_until_now):
        if root is None:
            return 0
        cur_sum = sum_until_now*10 + root.val
        if root.left is None and root.right is None:
            return cur_sum
        return self.total_sum(root.left, cur_sum) + self.total_sum(root.right, cur_sum)
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.total_sum(root, 0)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_sum(self, root, cur, root_to_leaf):
        if root is None: return
        cur = cur*10 + root.val
        if root.left is None and root.right is None:
            root_to_leaf.append(cur)
        else:
            self.find_sum(root.left, cur, root_to_leaf)
            self.find_sum(root.right, cur, root_to_leaf)
        cur = cur/10 - root.val

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_to_leaf = []
        self.find_sum(root, 0, root_to_leaf)
        return sum(root_to_leaf)
        
