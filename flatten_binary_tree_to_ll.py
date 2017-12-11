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
    def flatten_bst(self, root)
        '''
        Similar version of the problem: http://www.geeksforgeeks.org/convert-a-given-binary-tree-to-doubly-linked-list-set-2/
        https://articles.leetcode.com/convert-binary-search-tree-bst-to/
        '''
        pass

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        Idea: https://discuss.leetcode.com/topic/3995/share-my-simple-non-recursive-solution-o-1-space-complexity
        This traversal is very similar to morris traversal used for traversing a tree without recursion/stack
        """
        now = root
        while now:
            if now.left:
		# Find current node's prenode that links to current node's right subtree
                pre = now.left
                while pre.right:
                    pre = pre.right
                pre.right = now.right
		"""
		Use current node's left subtree to replace its right subtree(original right 
                subtree is already linked by current node's prenode
		"""
                now.right = now.left
                now.left = None
            else:
                now = now.right

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
