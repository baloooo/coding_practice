'''
https://discuss.leetcode.com/topic/40924/java-recursive-o-logn-space-and-iterative-solutions-o-1-space-with-explanation-and-figure
https://discuss.leetcode.com/topic/26276/explain-the-question-and-my-solution-python/7
'''


class Solution():
    def upsideDownBinaryTree(self, root):
        if root is None or root.left is None:
            return root

        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right   # node 2 left children
        root.left.right = root        # node 2 right children
        root.left = None
        root.right = None
        return newRoot
