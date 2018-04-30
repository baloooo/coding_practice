"""
.
"""


def k_smallest_naive(k):
    """
     1. inorder O(n)
     2. find element by arr[-k] O(1)
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
        Strategy:
        
        Idea is to keep a counter in the #logic area of inorder traversal and the moment it
        reaches target(depending you're decrementing to 1 or incremting to k) you can start
        returning the node.val.

        Regular inorder, Basic idea is to Go left, decrement k, Go right
        
        At any stage if k == 1, meaning we found our target keep returning that val back.
        If there are multiple insertion/deletion of nodes and we need to calculate kthsmallest frequently, we should
        start storing count of nodes in left subtree at every nodes, which can easiliy be maintained while creation/deletion
        and easy to access too.

        Time: O(max(h,k))
        Space: O(h)
        https://discuss.leetcode.com/topic/17810/3-ways-implemented-in-java-python-binary-search-in-order-iterative-recursive/75
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
