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


class Solution:

    def __init__(self, root):
        self.min_stack = []
        self.max_stack = []
        self._populate_min_stack(root)
        self._populate_max_stack(root)

    def _populate_min_stack(self, root):
        if root is None:
            return
        if root.right:
            if root.left:
                self.min_stack.append(root.right)
                self.min_stack.append(root.val)
                self._populate_min_stack(root.left)
            else:
                self._populate_min_stack(root.right)
                self.min_stack.append(root.val)
        else:
            self.min_stack.append(root.val)
            self._populate_min_stack(root.left)

    def _populate_max_stack(self, root):
        if root is None:
            return
        if root.left:
            if root.right:
                self.max_stack.append(root.left)
                self.max_stack.append(root.val)
                self._populate_max_stack(root.right)
            else:
                self._populate_max_stack(root.left)
                self.max_stack.append(root.val)
        else:
            self.max_stack.append(root.val)
            self._populate_max_stack(root.right)

    def _next_min(self):
        top_of_min_stack =  self.min_stack.pop()
        if isinstance(top_of_min_stack, Node):
            self._populate_min_stack(top_of_min_stack)
            return self.min_stack.pop()
        else:
            return top_of_min_stack

    def _next_max(self):
        top_of_max_stack = self.max_stack.pop()
        if isinstance(top_of_max_stack, Node):
            self._populate_max_stack(top_of_max_stack)
            return self.max_stack.pop()
        else:
            return top_of_max_stack

    def two_sum_exists(self, target_num):
        min_ele = self._next_min()
        max_ele = self._next_max()
        while (1):
            cur_sum = min_ele + max_ele
            if cur_sum == target_num:
                return True
            try:
                if cur_sum < target_num:
                    min_ele = self._next_min()
                else:
                    max_ele = self._next_max()
            except IndexError:
                return False
        return False


if __name__ == '__main__':
    from tree_base import level_order_array_to_tree, Node
    arr = [100, 50, 150, 25, 75, 125, 175]
    root = level_order_array_to_tree(arr) 
    sol = Solution(root)
    print sol.two_sum_exists(1)
