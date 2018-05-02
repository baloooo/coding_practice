# coding: utf-8
from tree_base import level_order_array_to_tree


class Solution(object):
	'''
	Idea: For every node,
		length of longest path which pass it = MaxDepth of its left subtree + MaxDepth of its right subtree.
	therefore calculate longest path which passes each node and match it with longest seen path until now.
	Now return the max depth of left and right subtree as the max can be used by a node above to make
	a longest node path.

	https://leetcode.com/problems/diameter-of-binary-tree/discuss/101132/Java-Solution-MaxDepth
	'''
    def dfs(self, root):
        if root is None: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        cur_node_max_len = left+right
        self.max_len = max(self.max_len, cur_node_max_len)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0
        self.dfs(root)
        return self.max_len


class Solution:
    def __init__(self):
        self.left_most_point = 0
        self.right_most_point = 0

    def get_diameter(self, root):
        self.find_diameter(root, 0)
        return abs(self.left_most_point - self.right_most_point)

    def find_diameter(self, root, cur_val):
        if root is None:
            return
        if cur_val < self.left_most_point:
            self.left_most_point = cur_val
        self.find_diameter(root.left, cur_val-1)
        if cur_val > self.right_most_point:
            self.right_most_point = cur_val
        self.find_diameter(root.left, cur_val+1)

if __name__ == '__main__':
    arr = [3, 6, 8, 2, 11, None, 13, None, None, 9, 5, 7, None]
    root = level_order_array_to_tree(arr)
    print Solution().get_diameter(root)
