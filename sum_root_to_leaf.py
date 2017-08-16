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
