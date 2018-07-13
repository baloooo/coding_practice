# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
		https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98779/Right-to-Left-BFS-(Python-+-Java)
		The idea is to do a BFS traversal but add right branch first, this makes sure left subtree is dealt last. Also since
		we're doing BFS the last row in queue will be the bottom most queue and inserting right first makes sure we'll deal
		with left most node last and therefore we can safely return the last node to be dealt in a BFS right to left traversal
		of the tree.
        """
        from Queue import Queue
        bfs_q = Queue()
        bfs_q.put(root)
        cur = None
        while not bfs_q.empty():
            cur = bfs_q.get()
            if cur.right:
                bfs_q.put(cur.right)
            if cur.left:
                bfs_q.put(cur.left)
            
        return cur.val if cur is not None else None
