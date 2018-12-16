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
    def _join(self, a, b):
        '''
        helper function -- given two list nodes, join them
        together so the second immediately follow the first.
        Sets the .next of the first and the .previous of the second.
        '''
        a.right = b
        b.left = a

    def _append(self, l1, l2):
        '''
        Appends two circular doubly linked lists l1 and l2 as one circular double LL.
        @returns 
        ---------------
        |             |
        <- l1 <-> l2 ->
        '''
        if l1 is None:
            reutrn l2
        if l2 is None:
            return l1
        # since l1 is a circular doubly LL, head's left points to tail/end of the Linked List.
        l1_end = l1.left
        l2_end = l2.left

        self.join(l1_end, l2)
        self.join(l2_end, l1)

        return l1

    def tree_to_list(self, root):
        '''
        Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the
        previous and next pointers in a doubly-linked list.
        https://articles.leetcode.com/convert-binary-search-tree-bst-to/
        http://cslibrary.stanford.edu/109/TreeListRecursion.html
        https://www.youtube.com/watch?v=Dte6EF1nHNo
        converts a binary tree to circular doubly linked list.
        '''
        if root is None:
            return
        left_list = self.tree_to_list(root.left) # should construct and return a List from left side of the tree
        right_list = self.tree_to_list(root.right)
        '''
        Since _append method expects circular linked lists we will make root node in to circular
        doubly linked list.
        '''
        root.left = root
        root.right = root
        # Concatenate left and right lists with root.
        root = self._append(left_list, root)
        root = self._append(root, right_list)

        return root

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

if __name__ == '__main__':
    arr = [1, 2, 5, 3, 4, 6, 7]
    arr = [1]
    from tree_base import print_tree_dfs, level_order_array_to_tree
    root = level_order_array_to_tree(arr) 
    Solution().flatten_binary_tree(root)
    print_tree_dfs(root)
