"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


class Solution:
    def __init__(self):
        pass

    def level_order(self, root):
        if not root:
            return []
        all_nodes, next_level = [], [root]
        while next_level:
            print next_level
            all_nodes.append([node.val for node in next_level])
            next_level = [child for node in next_level for child in [node.left, node.right] if child]  # noqa
        return all_nodes

if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    arr = [1, 2, 3, 4]
    root = level_order_array_to_tree(arr)
    print Solution().level_order(root)
