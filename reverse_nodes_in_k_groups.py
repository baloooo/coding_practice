"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # verify if k nodes exist.
        # reverse k nodes
        # link head of this group to next group and tail of this group to head of prev group
        cur_node = jump = ListNode('-1')
        # l and r are the limits in which nodes need to be reversed
        cur_node.next = l = r = head
        count = 0
        while True:
            # Move r one step over, so as to land it on the next node of k group nodes which then can be used to connect prev grp
            while count < k and r:
                r = r.next
                count += 1
            if count == k:
                # reverse k nodes
                # set pre to next groups head node, which is intentionally where r is sitting.
                pre, cur = r, l
                while count > 0:
                    next = cur.next
                    cur.next = pre # (1)
                    pre = cur
                    cur = next
                    count -= 1
                # set cur_node.next to pre which is joining prev tail to currently reversed group head
                # set cur_node to l to point it now at the previous goups tail( notice l points to tail now since this group is now reversed)
                # set r to l this will be the pre or head of prev reversed group which willl be set to next groups tail in (1)
                cur_node.next, cur_node, l = pre, l, r
            else:
                return jump.next
