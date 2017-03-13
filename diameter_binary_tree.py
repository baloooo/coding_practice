# coding: utf-8
from tree_base import level_order_array_to_tree


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
