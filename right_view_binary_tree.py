# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    In general top view is vertical order traversal of tree.
    Left and right view are covered here.
    Bottom view is returning all leaf nodes.
    Also do look at tree_boundary example, problem statement is slightly different from view but gives a nice
    complete view.

    Time and space for all the variations is O(n).
    Iterative implementation at the bottom(probably the most intutive and efficient as uses heap's stack rather than internal stack which
    is limited)
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

##################################################################
'''
Alternate method: Idea is to create a map of depth to node, every time we see a new depth we add the node we are at,
since we're visiting right first every time we see a new depth the node will be the one seen from right view.
'''
def get_rv(self, root, cur_depth, right_view):
    if root is None: return
    if cur_depth not in right_view:
        right_view[self.depth] = root

    self.get_rv(root.right, cur_depth+1,right_view)

    self.get_rv(root.left, cur_depth+1,right_view)

def get_right_view(self, root):

    right_view = {}
    self.get_rv(root, -1, right_view)
    return [right_view[num] for num in sorted(right_view.keys())]

#######################################################################################################################################
'''
iterative implementation of the same idea.
'''

def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None: return []
    stack = [(root, 0)]
    right_view = {}
    while stack:
        node, depth = stack.pop()
        if depth not in right_view:
            right_view[depth] = node.val
        if node.left is not None:
            stack.append((node.left, depth + 1))
        if node.right is not None:
            stack.append((node.right, depth + 1))

    return [right_view[num] for num in sorted(right_view.keys())]