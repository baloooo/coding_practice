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
from tree_base import Node


def build_tree(inorder, postorder, left_post, right_post, k):
    k -= 1
    target = postorder[k]
    target_index = inorder.index(target)
    root = Node(target)
    root.left = build_tree(inorder, postorder, left_post, target_index-1, k)
    root.right = build_tree(inorder, postorder, target_index+1, right_post, k)
    return root

if __name__ == '__main__':
    inorder, postorder = [], []
    build_tree(inorder, postorder, 0, len(postorder)-1, len(postorder)-1)
