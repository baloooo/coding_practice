"""
Given a binary search tree, write a function to find the kth smallest element
in the tree.

Example :

Input :
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST
"""


def k_smallest_naive(k):
    """
     1. inorder O(n)
     2. find element by arr[-k] O(1)
     3. find in bst O(logn)
     Total: Time: O(n), space: O(n)
    """
    pass


class Solution(object):

    def __init__(self):
        self.count = 0

    def k_smallest_optimized_recursive(self, root, k):
        """
        Time: O(max(h,k))
        Space: O(h)
        """
        return self.inorder(root, k)

    def inorder(self, root, k):
        if root is None:
            return
        val = self.inorder(root.left, k)
        if val is not None:
            return val
        self.count += 1
        if self.count == k:
            return root.val
        else:
            val = self.inorder(root.right, k)
            if val is not None:
                return val


if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    arr = [4, 2, 6, 1, 3, 5, 7]
    # arr = [1]
    # arr = [3, 2, None]
    # arr = [3, None, 4]
    root, k = level_order_array_to_tree(arr), 2
    sol = Solution()
    print sol.k_smallest_optimized_recursive(root, k)
