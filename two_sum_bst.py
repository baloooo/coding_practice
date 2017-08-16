# coding: utf-8
"""
Given a binary search tree T, where each node contains a positive integer, and
an integer K, you have to find whether or not there exist two different nodes A
and B such that A.value + B.value = K.

Return 1 to denote that two such nodes exist. Return 0, otherwise.

Notes
- Your solution should run in linear time and not take memory more than
    O(height of T).
- Assume all values in BST are distinct.

Example :

Input 1:

T :       10
         / \
        9   20

K = 19

Return: 1

Input 2:

T:        10
         / \
        9   20

K = 40

Return: 0
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def push_all_min(self, root):
        while root is not None:
            self.min_stack.append(root)
            root = root.left
    def push_all_max(self, root):
        while root is not None:
            self.max_stack.append(root)
            root = root.right
    def next_min(self):
        cur_min = self.min_stack.pop()
        self.push_all_min(cur_min.right)
        return cur_min
    def next_max(self):
        cur_max = self.max_stack.pop()
        self.push_all_max(cur_max.left)
        return cur_max
    def custom_init(self, root):
        self.min_stack = []
        self.max_stack = []
        self.push_all_min(root)
        self.push_all_max(root)
    def findTarget(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.custom_init(root)
        cur_min = self.next_min()
        cur_max = self.next_max()    
        while cur_min != cur_max:
            cur_sum = cur_min.val + cur_max.val
            if cur_sum == target:
                return True
            if cur_sum < target:
                cur_min = self.next_min()
            else:
                cur_max = self.next_max()
        return False


if __name__ == '__main__':
    from tree_base import level_order_array_to_tree, Node
    arr = [100, 50, 150, 25, 75, 125, 175]
    root = level_order_array_to_tree(arr) 
    sol = Solution(root)
    print sol.two_sum_exists(1)
