# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = start = ListNode('dummy')
        dummy.next = head
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                # since we cannot move backwards in LL, always have a pointer at the beginning.
                start = dummy
                while start.next.val < head.next.val:
                    start = start.next
                # Linking head.next(target) to start.next (approporiate location) and so on.
                # using one liner to alleviate the need of temp. variables
                # move
                start.next, head.next.next, head.next = head.next, start.next, head.next.next
        return dummy.next
