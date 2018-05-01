# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if self.pre and self.pre.val > root.val:
            # Notice: the first time an anomaly is encountered our target is in first node self.pre,
            # whereas for the second node our target will be in latter node therefore in root
            if self.first is None:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inorder(root.right)
            
    def recoverTree(self, root):
        """
        Time: O(n) Space: O(h) stack space
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
	Idea: https://discuss.leetcode.com/topic/3988/no-fancy-algorithm-just-simple-and-powerful-in-order-traversal/63
        Idea: The naive version of this idea can be to do an inorder traversal of the BST.
        Store the result in an array and go over the array to find the two anomaly elements.
        The exact same logic can be used to do it in place.
        Take the inorder arr =[25, 50, 75, 100, 125, 150, 175] and let after a swap the new arr is
        [25, 125, 75, 100, 50, 150, 175], now if you use temp variables to track anomalies.
        (prev_ele, cur_root, first_ele, second_ele)
        You'll find that the anomaly condition is "if prev_ele > cur_root" there is an anomaly
        b'coz in sorted array always previous element should be less than current element.
        Note: Also if you run thru this array once you will find that first element will end up in prev_ele
        variable and second element will end up in root element.
        Once you've both elements you can just swap the values and very similar in tree swap
        the values of two nodes(we don't need to swap the entire nodes with mappings just the values)
        Edge case: There can be situations where there the anomalies are together(parent-child)
        [3,1,4,null,null,2] which gives inorder [1, 3, 2, 4], for situations like this we always
		assign first, second together as is more evident from solution below so incase there is no
		second anomaly we will know that the first one had consecutive anomalies.
        """
        self.first = self.second = self.pre = None
        self.inorder(root)
        if self.first is not None:
            self.first.val, self.second.val = self.second.val, self.first.val

class Solution(object):
	'''
	The idea is same as above just a slightly different way of implementation
	'''
    def inorder(self, root):
        if root is None: return root
        self.inorder(root.left)
        # logic
        if self.first is None and self.prev.val > root.val:
            self.first = self.prev
		# Notice that this is an if and not elif, so when arr=[1, 3, 4, 2] and we find the first
		# anomaly at prev=3 and root=2 we set both first and second at that point itself.
        if self.first is not None and self.prev.val > root.val:
            self.second = root
        self.prev = root
        self.inorder(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode(-float('inf'))
        self.first = self.second = None
        self.inorder(root)
        if self.second is not None:
            self.first.val, self.second.val = self.second.val, self.first.val
