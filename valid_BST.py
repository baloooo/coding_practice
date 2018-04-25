# -*- coding: utf-8
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the
node’s key.
The right subtree of a node contains only nodes with keys greater than the
node’s key.
Both the left and right subtrees must also be binary search trees.
Example :

Input :
   1
  /  \
 2    3

Output : 0 or False


Input :
  2
 / \
1   3

Output : 1 or True
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
from tree_base import array_to_tree, print_tree_dfs, level_order_array_to_tree
'''
Idea is to pass upper and lower bound limits for every root down to every subtree within a tree.
At every root depending on whether we go left or right we'll modify the bounds for ex: when we
go left we're bounded by upper limit of root on all the subtrees on LHS of the root and so on.
And any place in the subtress where the condition lower_bound < root.val < upper_bound is violated
we return False.
'''

class Solution(object):
    def dfs(self, root, lower_bound, upper_bound):
        if root is None:
            return True
        if lower_bound < root.val < upper_bound:
            return self.dfs(root.left, lower_bound, root.val) and self.dfs(root.right, root.val, upper_bound)
        else:
            return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Time: O(n)
        space: O(logn) // stack space
        """
        return self.dfs(root, -float('inf'), float('inf'))

def is_bst(root):
    def valid_bst(root, min_val, max_val):
        if root is None:
            return True
        if root.val >= max_val or root.val < min_val:
            return False
        return valid_bst(root.left, min_val, root.val) and valid_bst(root.right, root.val, max_val)
    return int(valid_bst(root, float('-inf'), float('inf')))


if __name__ == '__main__':
    arr = [1, 5, 5, 2, 2, None, 3]
    # root = array_to_tree(arr)
    # arr = [100, 50, 150, None, 75, 125, None]
    arr = [3,2,4,1,3,None,None,None,None,None,None]
    root = level_order_array_to_tree(arr)
    print_tree_dfs(root)
    print is_bst(root)
