https://discuss.leetcode.com/topic/7031/simple-java-solution-in-one-pass/42
https://discuss.leetcode.com/topic/14692/3-short-python-solutions/8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = orig_head = ListNode('dummy')
        orig_head.next = head
        # Move fast in front so that the gap between slow and fast becomes n
        for _ in xrange(n):
            fast = fast.next
        # Move fast to the end, maintaining the gap
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        # Skip the desired node
        slow.next = slow.next.next
        return orig_head.next
