"""
Given a sorted linked list, delete all duplicates such that each element appear
only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        orig_head = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return orig_head
"""
Extension of above
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Idea: Outside loop for traversing LL and inside loop for removing duplicates
        """
        orig_head = pre = ListNode(float('inf'))
        pre.next = head
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if pre.next != head:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return orig_head.next
