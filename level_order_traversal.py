# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        cur_level, lvl_order_result = [root], []
        while cur_level:
            cur_level_nodes = []
            next_level = []
            for node in cur_level:
                cur_level_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
            lvl_order_result.append(cur_level_nodes)
        return lvl_order_result
