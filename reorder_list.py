# coding: utf-8
"""
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

from linkedlistbase import construct_linked_list_from_array, compare_two_linked_lists

class Solution:
    def reorder_list2(self, head):
        if not head or not head.next:
                return
        # find mid
        orig_head = fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse all nodes from mid to len
        # reverse the second half in-place
        prev, cur, next = None, slow, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # prev has the last node now
        # Merge in-place; Note : the last node of second is None now since we reverted the second half.
        first, second = orig_head, prev
        while second.next:
            first.next, first = second, first.next # Note: first, first.next doesn't work for LHS
            second.next, second = first, second.next 
        return

    def reorder_list(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
	# find half
	# reverse nodes from mid point onwards
	# traverse up to mid point and keep alternating nodes with second half of LL
        if head is None:
            return
        if head.next is None:
            return head
        slow = slow_pre = fast = orig_head = head
        while fast and fast.next:
            slow_pre = slow
            slow = slow.next
            fast = fast.next.next
        pre = None
        while slow:
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        slow_pre.next = pre
        slow_pre = slow_pre.next
        # 1->2->4->3
        # slow_pre = 4
        # first, second = head, 
        # while slow_pre.next is not None:
        #     slow_next = slow_pre.next
        #     head_next = head.next
        #     head.next = slow_pre
        #     slow_pre.next = head_next
        #     slow_pre = slow_next
        #     head = head_next
        # slow_next = slow_pre.next
        # head_next = head.next
        # head.next = slow_pre
        # import ipdb; ipdb.set_trace()
class Solution(object):
	def find_mid(self, head):
		slow = fast = prev_tail = head
		while fast and fast.next:
			prev_tail = slow
			slow = slow.next
			fast = fast.next.next
		prev_tail.next = None
		return slow

	def reverse(self, cur):
		prev = None
		while cur:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		return prev

	def reorder(self, left_head, right_head):
		while left_head and right_head:
			left_head.next, left_head, left_head_copy = right_head, left_head.next, left_head
			if left_head is None:
				return
			right_head.next, right_head = left_head, right_head.next
		
    def reorderList(self, head):
        """
		Alternate way, a little more modular
        """
        right_half_head = self.find_mid(head)
        right_half_head = self.reverse(right_half_head)
        self.reorder(head, right_half_head)


if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2], [1, 2]),
        ([1], [1]),
    ]
    head = construct_linked_list_from_array(test_cases[2][0])
    res = Solution().reorder_list2(head)
    # for index, test_case in enumerate(test_cases, 1):
    #     head = construct_linked_list_from_array(test_case[0])
    #     res = Solution().reorder_list(head)
    #     expected_res = construct_linked_list_from_array(test_case[1])
    #     if compare_two_linked_lists(res, expected_res):
    #         print "%d: Passed" % index
    #     else:
    #         print "%d: Failed" % index
