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


class Solution:

    def zig_zag(self, root):
        cur_level = [root]
        res = []
        index = 0
        while cur_level:
            next_level = []
            cur_level_nodes = []
            for node in cur_level:
                cur_level_nodes.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            if index % 2 == 0:
                res.append(cur_level_nodes)
            else:
                res.append(cur_level_nodes[::-1])
            index += 1
            cur_level = next_level
        return res

if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    arr = [3, 9, 20, None, None, 15, 7]
    root = level_order_array_to_tree(arr)
    print Solution().zig_zag(root)
