"""
Time:  O(n)
Space: O(n)

Given a binary tree, return the bottom-up level order traversal of its nodes'
values.
 (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


def bottom_up_level_order(root):
    cur_level = [root]
    next_level = []
    res = []
    while cur_level:
        next_level = []
        cur_level_nodes = []
        for node in cur_level:
            cur_level_nodes.append(node.val)
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        cur_level = next_level
        res.append(cur_level_nodes)
    return res[::-1]

if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    arr = [3, 9, 20, None, None, 15, 7]
    root = level_order_array_to_tree(arr)
    print bottom_up_level_order(root)
