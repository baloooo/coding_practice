# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root):
        if root is None: return
        self.inorder(root.left)
        # Logic
        if root.val != self.cur_mode_val:
            if self.cur_mode_count > self.global_mode_count:
                self.modes = [self.cur_mode_val]
                self.global_mode_count = self.cur_mode_count
            elif self.cur_mode_count == self.global_mode_count:
                self.modes.append(self.cur_mode_val)
            self.cur_mode_val = root.val
            self.cur_mode_count = 1    
        else:
            self.cur_mode_count += 1

        self.inorder(root.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
		The idea is to traverse BST in inorder, thereby using the sorted list to find the mode.
		A mode in a sorted list can be found by keeping a running frequency count of numbers and doing
		the appropriate book keeping alongside.
        """
        self.modes = []
        self.global_mode_count = 0
        self.cur_mode_val = None
        self.cur_mode_count = -1
        self.inorder(root)
        if self.cur_mode_count > self.global_mode_count:
            self.modes = [self.cur_mode_val]
            self.global_mode_count = self.cur_mode_count
        elif self.cur_mode_count == self.global_mode_count:
            self.modes.append(self.cur_mode_val)
        return self.modes
