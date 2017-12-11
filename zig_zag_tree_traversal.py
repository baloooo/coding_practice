# coding: utf-8
"""
Given a binary tree, return the zigzag level order traversal of its nodes’
values. (ie, from left to right, then right to left for the next level and
alternate between).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
	Idea: very similar to level order tree traversal
        """
        if root is None:
            return []
        cur_level, lvl_order_result, zig_zag = [root], [], False
        while cur_level:
            cur_level_vals = []
            next_level = []
            for node in cur_level:
                cur_level_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
            if zig_zag:
                lvl_order_result.append(cur_level_vals[::-1])
            else:
                lvl_order_result.append(cur_level_vals)
            zig_zag = not zig_zag
        return lvl_order_result
        

if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    arr = [3, 9, 20, None, None, 15, 7]
    root = level_order_array_to_tree(arr)
    print Solution().zig_zag(root)
