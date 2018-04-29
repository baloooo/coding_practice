"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


class Solution(object):
    def check(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.check(root1.left, root2.right) and self.check(root1.right, root2.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        # As root is always symmetric bisect from start
        return self.check(root.left, root.right)

class Solution(object):
    def get_symmetric(self, left, right):
        if left is None or right is None:
            return left == right
        else:
            return (
		left.val == right.val and
		self.get_symmetric(left.left, right.right) and
		self.get_symmetric(left.right, right.left))
            
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.get_symmetric(root, root)
