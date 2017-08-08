class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        Idea: https://discuss.leetcode.com/topic/9557/clear-and-short-python-o-2n-and-o-n-solution/6
        Time: O(n) space: O(n)
        """
        if not head:
            return
        nodes_map = {}
        base = head
        while base:
            nodes_map[base] = RandomListNode(base.label)
            base = base.next
        base = head
        while base:
            nodes_map[base].next = nodes_map.get(base.next)
            nodes_map[base].random = nodes_map.get(base.random)
            base = base.next
        return nodes_map[head]

    
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        Time: O(n) Space: O(1)
        Idea: https://discuss.leetcode.com/topic/7594/a-solution-with-constant-space-complexity-o-1-and-linear-time-complexity-o-n
        """
        if not head:
            return
        # Insert copies in original linkedlist
        orig_head = head
        while head:
            copy = RandomListNode(head.label)
            temp = head.next
            head.next = copy
            copy.next = temp
            head = temp
        # Set random links on copy nodes
        head = orig_head
        while head:
            if head.random is not None:
                head.next.random = head.random.next
            head = head.next.next
        # seggregate original and copy linkedlists
        head = orig_head
        orig_head = cur = RandomListNode('-1')
        while head:
            cur.next = head.next
            head.next = head.next.next
            head = head.next
            cur = cur.next
        cur.next = None
        return orig_head.next
