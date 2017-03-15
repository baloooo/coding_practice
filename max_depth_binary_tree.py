"""
Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest
path from the root node down to the farthest leaf node.

 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
max depth = 2
"""
from tree_base import level_order_array_to_tree


def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == '__main__':
    arr = [1, 2, None, 3, None, 4, None]
    root = level_order_array_to_tree(arr)
    print max_depth(root)
