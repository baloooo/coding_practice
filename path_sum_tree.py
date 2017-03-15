"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Example :

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
from tree_base import level_order_array_to_tree


def tree_path_sum(root, target_sum):
    if root is None:
        return False
    # if (target_sum-root.val) < 0:
    #     return False
    if target_sum == root.val and root.left is None and root.right is None:
        return True
    target_sum -= root.val
    if tree_path_sum(root.left, target_sum):
        return True
    if tree_path_sum(root.right, target_sum):
        return True
    return False


if __name__ == '__main__':
    target_sum, arr = 22, [5, 4, 8, 11, 13, 4, 7, 2, None, None, None, 1]
    # target_sum, arr = 0, [0, None, None]
    # target_sum, arr = 1000, [1000, 200, None, None, None]
    # target_sum, arr = 2, [2]
    root = level_order_array_to_tree(arr)
    print tree_path_sum(root, target_sum)
