"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def inorder(self, cur):
        if cur is None: return
        self.inorder(cur.left)

        self.prev.right = cur
        cur.left = self.prev
        self.prev = cur

        self.inorder(cur.right)

    def treeToDoublyList(self, root):
        """
        https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/discuss/149151/Concise-Java-solution-Beats-100
        """
        if root is None: return
        dummy_node = Node('dummy', None, None)
        self.prev = dummy_node
        self.inorder(root)
        # link dummy_node.right and last node
        dummy_node.right.left, self.prev.right = self.prev, dummy_node.right
        return dummy_node.right