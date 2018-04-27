# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    Couple of solutions for the exercise
    https://leetcode.com/problems/binary-tree-right-side-view/solution/
    '''

    def dfs(root, cur_depth, view):
        if cur_depth > self.max_depth:
            view.append(root.val)
            self.max_depth = cur_depth
        self.dfs(root.right, cur_depth+1, view)
        self.dfs(root.left, cur_depth+1, view)

    def rightSideView(self, root):
        """
		Idea: DFS with visiting right node before than left node, and adding the first visited node
		at every new depth.
		Notice we can just change the traversal behavior for left and then right to get the 
		left view
		Time: O(n)
		Space: O(n) stack space for tree traversal (which is kind of mandatory), depends on the structure
		of tree.
        """
        view = []
        self.max_depth = -1
        self.dfs(root, 0, view)
        return view

    def rightSideView(self, root):
        """
        Idea: level order traversal
		Time: O(n)
		Space: O(n), width of the tree
        """
        if root is None:
            return []
        cur_level, right_view = [root], []
        while cur_level:
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            right_view.append(cur_level[-1].val)
            cur_level = next_level
        return right_view
