import pytest

class Solution():
    def closestValue(self, root, target):
        # Definition for a binary tree node.
		# class TreeNode(object):
		#     def __init__(self, x):
		#         self.val = x
		#         self.left = None
		#         self.right = None
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
		https://leetcode.com/problems/closest-binary-search-tree-value/discuss/70327/4-7-lines-recursiveiterative-RubyC++JavaPython
        """
        closest = root.val
        while root:
            # closest = min((root.val, closest), key=lambda x: abs(target - x))
            closest = root.val if abs(target-root.val) < abs(target-closest) else closest
            root = root.left if target < root.val else root.right
        return closest

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        ([10, 20], 30),
        ([30, 40], 70),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.task(*args) == result
