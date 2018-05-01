# coding: utf-8
"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solution/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def push_all_min(self, root):
        while root is not None:
            self.min_stack.append(root)
            root = root.left
    def push_all_max(self, root):
        while root is not None:
            self.max_stack.append(root)
            root = root.right
    def next_min(self):
        cur_min = self.min_stack.pop()
        self.push_all_min(cur_min.right)
        return cur_min
    def next_max(self):
        cur_max = self.max_stack.pop()
        self.push_all_max(cur_max.left)
        return cur_max
    def custom_init(self, root):
        self.min_stack = []
        self.max_stack = []
        self.push_all_min(root)
        self.push_all_max(root)
    def findTarget_optimized(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        Time: O(n) Space: O(h)
        If you have a space constraint, use this one rather than the above one
        """
        self.custom_init(root)
        cur_min = self.next_min()
        cur_max = self.next_max()    
        while cur_min != cur_max: # as min and max cannot point to one single node.
            cur_sum = cur_min.val + cur_max.val
            if cur_sum == target:
                return True
            if cur_sum < target:
                cur_min = self.next_min()
            else:
                cur_max = self.next_max()
        return False

	def findTarget_bfs(self, root, target):
        """
        Time: O(n) Space: O(n)
        Idea: similar to array two sum, but doesn't benefits from the fact that the tree is BST
        """
        seen = set()
        queue = [root]
        while queue:
            nxt_level = []
            while queue:
                cur = queue.pop()
                if target - cur.val in seen:
                    return True
                else:
                    if cur.left is not None:
                        nxt_level.append(cur.left)
                    if cur.right is not None:
                        nxt_level.append(cur.right)
                seen.add(cur.val)
            queue = nxt_level
        return False

	def findTarget_naive(self, root, target):
		'''
		Idea is to do an inorder traversal of BST and store results in an array.
		And in the next step do a two pointer search from start and end of the array for the sum
		Time: O(n) space: O(n)
		'''
