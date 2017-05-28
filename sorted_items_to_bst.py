"""
Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.

 Balanced tree : a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
Example :


Given A : [1, 2, 3]
A height balanced BST  :

      2
    /   \
   1     3
"""
import math


# Definition for a binary tree node.
class TreeNode(object):
    def __str__(self):
        return "tree node_val is %d" % self.val

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_bst(self, arr, start, end):
        # Never use this conditional: if end < 0 or start >= len(arr):
        if start > end:
            return None
        mid = start + int(math.ceil((end-start)/2.0))
        mid_node = TreeNode(arr[mid])
        mid_node.left = self.get_bst(arr, start, mid-1)
        mid_node.right = self.get_bst(arr, mid+1, end)
        return mid_node

    def sortedArrayToBST(self, arr):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not len(arr):
            return []
        return self.get_bst(arr, 0, len(arr)-1)

    def get_ll_len(self, head):
        count = 0
        while head is not None:
            head = head.next
            count += 1
        return count

    def construct_bst(self, n):
        # Base case
        if n <= 0:
            return None
        # Recursively construct the left subtree
        left_node = self.construct_bst(n/2)
        # Allocate memory for root
        root_node = TreeNode(self.head.val)
        # print 'n: {0}, root_node: {1}, left_node: {2}'.format(n, root_node, left_node)
        # Link above constructed left subtree with root
        root_node.left = left_node
        # Change head pointer of Linked List for parent recursive calls
        self.head = self.head.next
        # print 'new_head ', self.head
        # Recursively construct the right subtree and link it with root 
        # The number of nodes in right subtree  is total nodes - nodes in 
        # left subtree - 1 (for root) which is n-n/2-1*/
        root_node.right = self.construct_bst(n-n/2-1)
        # print 'root_node right', root_node.right
        return root_node

    def sorted_linkedlist_to_bst(self, head):
        """
        Given a singly linked list where elements are sorted in ascending
        order, convert it to a height balanced BST.
        Definition for singly-linked list.
        class ListNode(object):
            def __init__(self, x):
                self.val = x
                self.next = None

        Definition for a binary tree node.
        class TreeNode(object):
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        """
        n = self.get_ll_len(head)
        self.head = head
        return self.construct_bst(n)

if __name__ == '__main__':
    arr = [0]
    arr = [1, 3]
    # res = Solution().sortedArrayToBST(arr)
    from linkedlistbase import construct_linked_list_from_array
    head = construct_linked_list_from_array([10, 20, 30, 40, 50, 60])
    head = construct_linked_list_from_array([1])
    res = Solution().sorted_linkedlist_to_bst(head)
    import ipdb; ipdb.set_trace()
