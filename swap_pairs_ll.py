"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Idea: https://discuss.leetcode.com/topic/10649/my-simple-java-solution-for-share/28
        """
        cur_node = ListNode('dummy')
        cur_node.next = head
        if not head or not head.next:
            return head
        new_head = head.next
        # dummy -> 1 -> 2 -> 3 -> 4
        # since we require two nodes to swap
        while cur_node.next and cur_node.next.next:
            first = cur_node.next
            second = first.next
            
            first.next = second.next
            second.next = first
            # These two are most important and tricky steps
            # Join prev tail with next head
            cur_node.next = second
            # Move cur forward in position for next swaps
            cur_node = first
        return new_head
