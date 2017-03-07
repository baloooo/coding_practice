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


def get_bst(arr):
    from math import ceil
    tree_root = None

    def construct_bst(root, arr, left, right):
        if left+1 == right:
            root.left = arr[left]
            return
        median = left + ceil((right-left)/2)
        if root is None:
            global tree_root
            tree_root = root = Node(arr[median])
        else:
            new_node = Node(arr[median])
            if root.left is None:
                root.left = new_node
            else:
                root.right = new_node
        construct_bst(root, arr, left, median-1)
        construct_bst(root, arr, median+1, right)
    construct_bst(tree_root, arr, 1, len(arr)-1)
    return tree_root


if __name__ == '__main__':
    arr = [1, 2, 3]
    arr = [10, 20, 30, 40, 50, 60]
    root = get_bst(arr)
    print_tree_dfs(root)
