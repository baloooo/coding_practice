# coding: utf-8
"""
Find largest distance
Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000)
nodes. The goal of the problem is to find largest distance between two nodes in
a tree. Distance between two nodes is a number of edges on a path between the
nodes (there will be a unique path between any pair of nodes since it is a tree
). The nodes will be numbered 0 through N - 1.

The tree is given as an array P, there is an edge between nodes P[i] and
i (0 <= i < N). Exactly one of the i’s will have P[i] equal to -1, it will be
root node.

    Example:
    If given P is [-1, 0, 0, 0, 3], then node 0 is the root and the whole tree
    looks like this:

          0
       /  |  \
      1   2   3
               \
                4

    One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the
    answer is 3. Note that there are other paths with maximal distance.
"""
"""
If a tree is given
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1(object):
    def get_diameter(self, root):
        """
        Basically this exercise boils down to finding height of the tree
        at every node. Max diameter or max length of path would be just
        sum of left subtree and right subtree which can be checked at every
        node and kept track of. Notice we would progress the recursion
        exactly like we would for finding height of the tree since for
        each subtree we want to find the max height.
        """
        if root is None:
            return 0
        left = self.get_diameter(root.left)
        right = self.get_diameter(root.right)
        self.max_diameter = max(left+right, self.max_diameter)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        self.get_diameter(root)
        return self.max_diameter

"""
if tree is given in parent array representation, and the tree is an
    "n-ary tree".
Input: parent[] = {1 5 5 2 2 -1 3}
Output: 5
The given array represents following Binary Tree
         5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6
"""


class Solution:
    def calculate_diameter(self, root, tree):
        left = right = 0
        # Because of n-ary tree
        children = [0]
        child_index = 0
        for index, val in enumerate(tree):
            if val == root:
                children[child_index] = self.calculate_diameter(index, tree)
                children.append(0)
                child_index += 1
        # Get first and second max in left and right respectively.
        for val in children:
            if val > right:
                left = right
                right = val
            elif val > left:
                left = val
        self.max_diameter = max(left+right, self.max_diameter)
        return 1 + max(left, right)

    def get_diameter(self, tree):
        self.max_diameter = 0
        for index, val in enumerate(tree):
            if val == -1:
                self.calculate_diameter(index, tree)
                return self.max_diameter

if __name__ == '__main__':
    test_cases = [
        ([1, 5, 5, 2, 2, -1, 3], 5),
        ([-1, 0, 0, 0, 3], 3),
    ]
    for test_case in test_cases:
        res = Solution().get_diameter(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
