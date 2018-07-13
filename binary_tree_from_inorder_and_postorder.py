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

    def get_tree(self, inorder, postorder, in_start, in_end):
        if in_start > in_end:
            return None
        root = TreeNode(postorder.pop()) # this is O(1)
        # in_root = inorder.index(root.val)
        in_root = self.find_target_index(inorder, root.val, in_start, in_end)

        root.right = self.get_tree(inorder, postorder, in_root+1, in_end)
        root.left = self.get_tree(inorder, postorder, in_start, in_root-1)
        return root
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
	Idea is to get the order of traversal from postorder/preorder and the structure of
	division of tree from inorder traversal.
	Also notice that in postorder right needs to be dealt with first and then left and 
	vice-versa in preorder/inorder combination
        Also be sure to use popping techique for postorder array as using an index is a little
        more tricky.
        """
        return self.get_tree(inorder, postorder, 0, len(inorder)-1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_index = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_index])
            # Trick here is to reverse the order of right child population in postorder creation than preorder creation so as 
            # to prevent Indexerrors
            root.right = self.buildTree(inorder[root_index+1:], postorder)
            root.left = self.buildTree(inorder[:root_index], postorder)
            return root

if __name__ == '__main__':
    inorder, postorder = [2, 1, 3], [2, 3, 1]
    inorder = [80, 40, 90, 20, 100, 50, 110, 10, 120, 60, 130, 30, 140, 70, 150]  # noqa
    post = [80, 90, 40, 100, 110, 50, 20, 120, 130, 60, 140, 150, 70, 30, 10]  # noqa
    inorder = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    root = Solution().build_tree(inorder, post, 0, len(inorder)-1, len(inorder))  # noqa
    print_tree_dfs(root)
