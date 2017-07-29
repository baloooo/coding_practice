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
        dummy = pre = ListNode(-1)
        cur = dummy.next = head
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                while pre.next.val < cur.next.val:
                    pre = pre.next
                our_node = cur.next
                cur.next = our_node.next
                temp = pre.next
                pre.next = our_node
                our_node.next = temp
            pre = dummy
        return dummy.next
