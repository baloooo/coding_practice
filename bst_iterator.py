"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

 Note: next() and hasNext() should run in average O(1) time and uses O(h)
"""
from tree_base import level_order_array_to_tree, Node


class Solution:

    def __init__(self, root):
        self.stack = []
        self._populate_stack(root)

    def _populate_stack(self, root):
        if root is None:
            return
        if root.left:
            if root.right:
                self.stack.append(root.right)
            self.stack.append(root.val)
            self._populate_stack(root.left)
        else:
            self._populate_stack(root.right)
            self.stack.append(root.val)

    def next(self):
        try:
            min_val = self.stack.pop()
        except IndexError:
            return -1
        if isinstance(min_val, Node):
            self._populate_stack(min_val)
            return self.stack.pop()
        else:
            return min_val
        

if __name__ == '__main__':
    arr = [100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, None, None, None, None]
    arr = [100, None, 150, None, 175]
    root = level_order_array_to_tree(arr)
    sol =  Solution(root)
    res = 0
    while res != -1:
        res = sol.next()
        print res
