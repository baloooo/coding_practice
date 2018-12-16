"""
Given a binary tree, determine if it is height-balanced.

 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 
"""
from tree_base import level_order_array_to_tree


def is_balance_binary_tree(root):
    # https://discuss.leetcode.com/topic/7798/the-bottom-up-o-n-solution-would-be-better/46
    # Here -1 means it's not balanced and is translated to False in base method.
    def height(root, cur_height):
        if root is None:
            return 0
        else:
            height_left_subtree = height(root.left, cur_height+1)
            height_right_subtree = height(root.right, cur_height+1)
            if height_left_subtree == -1 or height_right_subtree == -1:
                return -1
            elif abs(height_right_subtree - height_left_subtree) > 1:
                return -1
            else:
                return max(height_left_subtree, height_right_subtree)+1
    return 0 if height(root, 0) == -1 else 1


if __name__ == '__main__':
    from tree_base import print_tree_dfs, array_to_tree
    # arr = [3, 2, None, 1, None, None, None]
    # arr = [1, 2, 3]
    # arr = [3, 2, 4, 1, 3, None, None, 5]
    # arr = [50, 57, None, 55, 80]
    # arr = [None if x=='-1' else int(x) for x in arr_str.split(' ')]
    # root = level_order_array_to_tree(arr)
    arr = [-1, 0, 1, 2]
    root = array_to_tree(arr)
    # print_tree_dfs(root)
    print is_balance_binary_tree(root)
