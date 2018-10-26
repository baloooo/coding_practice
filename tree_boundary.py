'''
Note that we want left boundary and not left view
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.
Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

[1, 2, null, 3, null, 4, 7, 5, 6, 8, 9]
gives output [1, 2, 3, 4, 5, 6, 8, 9], notice that there is no 7 as that doesn't comes from root to right most node path since root.right is None.

but [1, 2, null, 3, null, null, 4, null, 5] will output [1, 2, 3, 4, 5] as expected since root.left can parse all the curves.
thereofore it's critical to understand the root.left to left_boundary idea.

Note: Left boundary is defined as the path from root to the left-most node.
Notice that this is not same as left view.
Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1
Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2
Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
'''


class Sol(object):
    '''
    Time: O(n)
    Space: O(n)
    https://leetcode.com/problems/boundary-of-binary-tree/discuss/101280/Java(12ms)-left-boundary-left-leaves-right-leaves-right-boundary

    https://leetcode.com/problems/boundary-of-binary-tree/solution/
    '''

    def is_leaf(self, root):
        if self.left is None and self.right is None:
            return True

    def get_left_boundary(self, root, left_boundary):
        # once we hit leaf node from root we have done traversing left boundary.
        while root is not None:
            if not self.is_leaf(root):
                # as we don't want to include leaves in left boundary.we have a separate check for them
                left_boundary.append(root.val)
            if root.left is not None:
                root = root.left
            else:
                root = root.right

    def get_right_boundary(self, root, right_boundary):
        while root is not None:
            if not self.is_leaf(root):
                right_boundary.append(root.val)
            if root.right is not None:
                root = root.right
            else:
                root = root.left

    def get_leaves(self, root, leaves):
        if root is None: return
        if self.is_leaf(root):
            leaves.append(root.val)
        self.get_leaves(root.left, leaves)
        self.get_leaves(root.right, leaves)

    '''
    One idea is to use:
        get left boundary, get leaves, get_right boundary.

    A more optimized version using flags can be found at: /solutions.
    '''

    def get_boundary(self, root):
        '''

        '''
        if root is None: return []
        left_boundary, leaves, right_boundary = [], [], []
        left_boundary.append(root.val)
        # get left view
        self.get_left_boundary(root.left, left_boundary)
        # get right view
        self.get_right_boundary(root.right, right_boundary)
        # get leaves
        self.get_leaves(root.left, leaves)
        self.get_leaves(root.right, leaves)
        return left_boundary + leaves + right_boundary[::-1]