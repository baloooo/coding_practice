# https://discuss.leetcode.com/topic/88520/python-straightforward-with-explanation-o-st-and-o-s-t-approaches
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def same_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
            return False
        '''
        Above can be replaced by, but is kept for easy understability
        if not(s and t):
            return s is t
        '''
        return (
            root1.val == root2.val and
            self.same_tree(root1.left, root2.left) and
            self.same_tree(root1.right, root2.right))

    def isSubtree1(self, s, t):
        """
        O(len(s) * len(t))
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.same_tree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
###############################################################################
    def _get_hash(self, x):
        from hashlib import sha256
        sha = sha256()
        sha.update(x)
        return sha.hexdigest()

    def add_merkle_hashes(self, node):
        if node is None:
            return '#' # Leaf nodes will be a hash(#node.val#) instead of dealing with None.
        node_left = self.add_merkle_hashes(node.left)
        node_right = self.add_merkle_hashes(node.right)
        node.merkle = self._get_hash(node_left + str(node.val) + node_right)
        return node.merkle

    def is_merkel_match(self, haystack, needle):
        '''
        Just runs thru s (haystack tree) to see if any node has
        the same merkel hash as root of t. The place it matches we can
        guarantee that entire tree under that matches exactly as t.
        '''
        if not haystack:
            return False
        return (
            haystack.merkle == needle.merkle or
            self.is_merkel_match(haystack.left, needle) or
            self.is_merkel_match(haystack.right, needle))

    def isSubtree(self, s, t):
        """
        Time: O(len(s) + len(t))
        Space: Extra merkle hash on each node on s and t
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.add_merkle_hashes(s)
        self.add_merkle_hashes(t)
        return self.is_merkel_match(s, t)
