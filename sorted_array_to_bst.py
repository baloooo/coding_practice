"""
Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.

 Balanced tree : a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
Example :


Given A : [1, 2, 3]
A height balanced BST  :

      2
    /   \
   1     3
"""
from tree_base import print_tree_dfs, Node


class Solution:
    def __init__(self):
        self.tree_root = None

    def get_bst(self, arr):
        from math import ceil

        def construct_bst(root, arr, left, right):
            if left == right:
                if root.left is None:
                    root.left = Node(arr[left])
                else:
                    root.right = Node(arr[left])
                return
            median = int(left + ceil((right-left)/2.0))
            if root is None:
                self.tree_root = root = Node(arr[median])
            else:
                new_node = Node(arr[median])
                if root.left is None:
                    root.left = new_node
                    root = root.left
                else:
                    root.right = new_node
                    root = root.right
            if left <= (median-1):
                construct_bst(root, arr, left, median-1)
            if median+1 <= right:
                construct_bst(root, arr, median+1, right)
        if len(arr) == 1:
            return Node(arr[0])
        construct_bst(self.tree_root, arr, 0, len(arr)-1)
        return self.tree_root


if __name__ == '__main__':
    # arr = [0, 1, 2, 3]
    # arr = range(15)
    arr = [0, 1]
    arr = [0, 1, 2]
    arr = [0]
    sol = Solution()
    root = sol.get_bst(arr)
    print_tree_dfs(root)
