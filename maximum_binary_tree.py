# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def build_tree(self, nums, start, end):
        if start > end: return
        max_index = start
        for i in xrange(start+1, end+1):
            if nums[i] > nums[max_index]:
                max_index = i
        root = TreeNode(nums[max_index])
        root.left = self.build_tree(nums, start, max_index-1)
        root.right = self.build_tree(nums, max_index+1, end)
        return root
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        Time: O(n^2)
        Space: O(h), stack space h is the height of the tree
        Very typical recursion problem where we divide the array in two parts in every recursion, based
        on the position of biggest num in the array. Catch being this could skew to O(n^2) worst case
        time complexity if the array is sorted.
        """
        return self.build_tree(nums, 0, len(nums)-1)

    def constructMaximumBinaryTree_optimized(self, arr):
        '''
        The key idea is:

        1. We scan numbers from left to right, build the tree one node by one step;
        2. We use a stack to keep some (not all) tree nodes and ensure a decreasing order;
        3. For each number, we keep pop the stack until empty or a bigger number.
        The bigger number (if exist, it will be still in stack) is current number's root,
        and the last popped number (if exist) is current number's left child (temporarily,
        this relationship may change in the future); Then we push current number into the stack.
        O(n) as every num in arr is added and popped exactly once.
        '''
        stack = []
        for num in arr:
            cur = TreeNode(num)
            '''
            If num is greater than max of everything we've seen untill now, attach last known max to current's left
            '''
            while stack and stack[-1].val < cur.val:
                cur.left = stack.pop()
            if stack:
                # if there's something on stack it has to be greater than cur therefore cur should be on to it's right
                # since cur comes positionally after element on the top of stack
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]

if __name__ == '__main__':
    arr = [3, 2, 1, 6, 0, 5]
    sol = Solution().constructMaximumBinaryTree_optimized(arr)
