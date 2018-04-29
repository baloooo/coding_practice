# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_max_sum(self, root):
        if root is None:
            return 0
        l = self.find_max_sum(root.left)
        r = self.find_max_sum(root.right)
        single_max = max(max(l, r)+root.val, root.val) # single arm max
        max_until_now = max(single_max, l+r+root.val) # max for current root
        self.max_sum = max(self.max_sum, max_until_now) # max until now
        return single_max 
        '''Note: We're returning single_arm_max and not max_untill now since singel_max is the
        one which ends at root, max_until_now extends to the other side so cannot be used by parent of 
        current root.
        Also note that we don't need to consider a case where only left subtree excluding cur root
        is compared since at any root it's current left subtree has already been completely dealt
        and max saved with so we don't need to bother with that at root.
        '''

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Idea: http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
        """
        self.max_sum = -float('inf')
        self.find_max_sum(root)
        return self.max_sum
