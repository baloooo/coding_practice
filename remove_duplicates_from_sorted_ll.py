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
                # Notice that you're still on head, your position changes only when distinct ele are encountered
                head.next = head.next.next
            else:
                head = head.next
        return orig_head

    def deleteDuplicates(self, head):
        orig_head = cur = ListNode(None)
        while head and head.next:
            if head.val != head.next.val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = head
        return orig_head.next

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
        Take two pointers prev and head, incase of duplicates traverse ahead using head, keep
        prev at last unique node position and jump it's next to first next unique node.
        and then continue as it is with prev -- head pointers one step at a time.
        """
        orig_head = pre = ListNode(float('inf'))
        pre.next = head
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if pre.next != head:
                # duplicates were encountered therfore set pre's next at next first unique node
                # notice pre pointer is still there and always point to one node behind head
                pre.next = head.next
            else:
                # No duplicates so just move pre one step forward
                pre = pre.next
            head = head.next
        return orig_head.next
