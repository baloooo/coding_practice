"""
Given a binary tree, flatten it to a linked list in-place.

Example :
Given


         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
"""

class Solution:

    def flatten_binary_tree(self, root):
        while(root is not None):
            if root.left is None:
                root = root.right
            elif root.right is None:
                root.right = root.left
                root.left = None
                root = root.right
            else:
                # Left and right both exists
                temp = root.right
                next_root = root.right = root.left
                root.left = None
                while root.right is not None:
                    root = root.right
                root.right = temp
                root = next_root


if __name__ == '__main__':
    arr = [1, 2, 5, 3, 4, 6, 7]
    arr = [1]
    from tree_base import print_tree_dfs, level_order_array_to_tree
    root = level_order_array_to_tree(arr) 
    Solution().flatten_binary_tree(root)
    print_tree_dfs(root)
