"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

 Note: next() and hasNext() should run in average O(1) time and uses O(h)
"""
from tree_base import level_order_array_to_tree, Node


class Solution:
    """
    Idea: https://discuss.leetcode.com/topic/6575/my-solutions-in-3-languages-with-stack/40
    """

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push_all(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        next_node = self.stack.pop()
        self.push_all(next_node.right)
        return next_node.val
    
    def push_all(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
        

if __name__ == '__main__':
    arr = [100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, None, None, None, None]
    arr = [100, None, 150, None, 175]
    root = level_order_array_to_tree(arr)
    sol =  Solution(root)
    res = 0
    while res != -1:
        res = sol.next()
        print res
