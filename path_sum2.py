# https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def path_sum_helper(self, root, target_sum, cur, path_sums):
        if root is None: return
        #self.cur.append(root.val)
        cur.append(root)
        if root.left is None and root.right is None:
            if target_sum - root.val == 0:
                # list(cur) or cur[::] was not working
                path_sums.append([node.val for node in cur])
        else:
            self.path_sum_helper(root.left, target_sum-root.val, cur, path_sums)
            self.path_sum_helper(root.right, target_sum-root.val, cur, path_sums)
        cur.pop()

    def pathSum(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        Idea: Key take aways is how temp. lists like cur and result list should
        be passed and dealt with. One shouldn't be setting these attributes on 
        the class itself which would make it accessible across all methods of the
        class and it's subclasses.
        """
        path_sums = []
        self.path_sum_helper(root, target_sum, [], path_sums)
        return path_sums

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorder(self, root, target_sum, cur, paths):
        if root is None: return 0
        if root.left is None and root.right is None and target_sum == root.val:
            cur.append(root.val)
            paths.append(cur[:])
            cur.pop()
            return
        cur.append(root.val)
        self.preorder(root.left, target_sum-root.val, cur, paths)
        self.preorder(root.right, target_sum-root.val, cur, paths)
        cur.pop()

    def pathSum(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        self.preorder(root, target_sum, [], paths)
        return paths
