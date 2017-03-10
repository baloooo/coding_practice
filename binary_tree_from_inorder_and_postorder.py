"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
Example :

Input :
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

Return :
            1
           / \
          2   3
"""
from tree_base import Node, print_tree_dfs


class Solution:
    def __init__(self):
        self.post_index = None

    def find_target_index(self, inorder, target, left_in, right_in):
        # this method can be replaced with a hash to get O(n) time complexity
        for index in xrange(left_in, right_in+1, 1):
            if inorder[index] == target:
                return index
        print 'target: {0} not found within left: {1} right: {2} in inorder'.format(target, left_in, right_in)  # noqa

    def build_tree(self, inorder, postorder, left_in, right_in, post_index):
        print 'left_in: {0} right_in: {1} post_index: {2}'.format(left_in, right_in, post_index)  # noqa
        if left_in == right_in:
            return Node(inorder[left_in])
        post_index -= 1
        target = postorder[post_index]
        target_index = self.find_target_index(
            inorder, target, left_in, right_in)
        root = Node(target)
        root.right = self.build_tree(
            inorder, postorder, target_index+1, right_in, self.post_index)
        root.left = self.build_tree(
            inorder, postorder, left_in, target_index-1, self.post_index)
        return root

if __name__ == '__main__':
    inorder, postorder = [2, 1, 3], [2, 3, 1]
    inorder = [80, 40, 90, 20, 100, 50, 110, 10, 120, 60, 130, 30, 140, 70, 150]  # noqa
    post = [80, 90, 40, 100, 110, 50, 20, 120, 130, 60, 140, 150, 70, 30, 10]  # noqa
    inorder = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    root = Solution().build_tree(inorder, post, 0, len(inorder)-1, len(inorder))  # noqa
    print_tree_dfs(root)
