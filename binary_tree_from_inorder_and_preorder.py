# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_tree(self, preorder, inorder, inorder_start, inorder_end):
        '''
        Note that since L.index(value, [start, [stop]]) -> integer -- return first index of value.
        where search continues excluding stop index similar to xrange, we always use one index extra
        as in root.left recursive call used root_index and not root_index-1 also from buildTree similar thing.
        '''
        if inorder_start >= inorder_end or self.preorder_index > len(preorder)-1: return None
        root = TreeNode(preorder[self.preorder_index])
        root_index = inorder.index(preorder[self.preorder_index], inorder_start, inorder_end)
        self.preorder_index += 1
        root.left = self.get_tree(preorder, inorder, inorder_start, root_index) # Note: root_index - 1 is not passed but root_index
        root.right = self.get_tree(preorder, inorder, root_index + 1, inorder_end)
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        Better to do this with indexes
        Time: O(n^2) as preorder is just traversed once left to right, and finding the index
        of preorder[preorder_index] in inorder should be O(n) amortized though will be highly
        contained as we're using indexes.

        Code: https://discuss.leetcode.com/topic/3695/my-accepted-java-solution
        Idea: https://discuss.leetcode.com/topic/21287/python-short-recursive-solution/10
        """
        if not preorder or not inorder: return
        self.preorder_index = 0
        return self.get_tree(preorder, inorder, 0, len(inorder)) # Note: len of inorder is passed not last index
        '''
        '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        The key idea is to make inorder and preorder arrays and broad tree construction template in mind.
        Idea: https://discuss.leetcode.com/topic/21287/python-short-recursive-solution/12
        """
        if inorder:
            cur_root_index = inorder.index(preorder.pop(0))
            cur_root = TreeNode(inorder[cur_root_index])
            cur_root.left = self.buildTree(preorder, inorder[:cur_root_index])
            cur_root.right = self.buildTree(preorder, inorder[cur_root_index+1:])
            return cur_root

