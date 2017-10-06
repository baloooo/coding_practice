# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution(object):
    def find_sum(self, root, target_sum, sum_until_now, prefix_sum):
        if not root: return
        sum_until_now = sum_until_now + root.val
        complement_sum = sum_until_now - target_sum
        if complement_sum in prefix_sum:
            self.paths += prefix_sum[complement_sum]
        prefix_sum[sum_until_now] += 1
        self.find_sum(root.left, target_sum, sum_until_now, prefix_sum)
        self.find_sum(root.right, target_sum, sum_until_now, prefix_sum)
        prefix_sum[sum_until_now] -= 1
            

    def pathSum(self, root, target_sum):
        """
        Idea: https://discuss.leetcode.com/topic/65100/python-solution-with-detailed-explanation/10
        """
        if not root: return 0
        self.paths = 0
        prefix_sum = collections.defaultdict(int)  # {prefix_sum untill this node: number of paths that have the same sum}
        sum_until_now = 0
        # Note: Adding this is very crucial, since when you start from a sub-tree,
        prefix_sum[0] = 1
        self.find_sum(root, target_sum, sum_until_now, prefix_sum)
        return self.paths
