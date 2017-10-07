"""
https://discuss.leetcode.com/topic/17810/3-ways-implemented-in-java-python-binary-search-in-order-iterative-recursive/75
If nodes can be altered frequently and this method needs to be called frequently. Just get the
inorder for the BST and get nodes from direct access, ofcourse given that O(n) space is not an
issue.
"""


def k_smallest_naive(k):
    """
     1. inorder O(n)
     2. find element by arr[-k] O(1)
     3. find in bst O(logn)
     Total: Time: O(n), space: O(n)
    """
    pass

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root):
        # Strategy:
        # Regular inorder, Basic idea is to Go left, decrement k, Go right
        # At any stage if k == 1, meaning we found our target keep returning that val back
        if root is None:
            return
        left = self.inorder(root.left)
        if left is not None:
            return left
        if self.k == 1:
            return root.val
        self.k -= 1
        return self.inorder(root.right)

    def kthSmallest(self, root, k):
        """
        Time: O(max(h,k))
        Space: O(h)
        """
        self.k = k
        return self.inorder(root)


if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    arr = [4, 2, 6, 1, 3, 5, 7]
    # arr = [1]
    # arr = [3, 2, None]
    # arr = [3, None, 4]
    root, k = level_order_array_to_tree(arr), 2
    sol = Solution()
    print sol.k_smallest_optimized_recursive(root, k)
