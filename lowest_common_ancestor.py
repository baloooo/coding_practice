# coding: utf-8
"""
Find the lowest common ancestor in an unordered binary tree given two values in the tree.

 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants. 
Example :


        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor 
Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.
"""
from tree_base import level_order_array_to_tree

class Solution:
    
    def lowest_common_ancestor(self, root, val1, val2):
        # Time: O(n) Space: O(1)
        # If val1, val2 are guaranteed to be in tree. (else you can run a search explicitly for their existence)
        if root is None:
            return
        if root.val in [val1, val2]:
            return root.val
        left_subtree = self.lowest_common_ancestor(root.left, val1, val2)
        right_subtree = self.lowest_common_ancestor(root.right, val1, val2)
        if (left_subtree == val1 and right_subtree == val2) or (left_subtree == val2 and right_subtree == val1):
            return root.val
        if left_subtree:
            return left_subtree
        if right_subtree:
            return right_subtree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
	# Notice p and q are tree nodes here and not values
        if root in [None, p, q]: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


if __name__ == '__main__':
    arr = [3, 6, 8, 2, 11, None, 13, None, None, 9, 5, 7, None]
    val1, val2, ans = 2, 5, 6
    root = level_order_array_to_tree(arr)
    # res = Solution().lowest_common_ancestor(root, val1, val2)
    # print res
    res = Solution2().lowest_common_ancestor(root, val1, val2)
    print res
    if res == ans:
        print "passed"
    else:
        print "failed"
