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
	if not head:
	    return
	# find the mid point
	slow = fast = head 
	while fast and fast.next:
	    slow = slow.next
	    fast = fast.next.next

	# reverse the second half in-place
	pre, node = None, slow
	while node:
	    import ipdb; ipdb.set_trace()	
	    pre, node.next, node = node, pre, node.next
	# Merge in-place; Note : the last node of "first" and "second" are the same
	first, second = head, pre
	while second.next:
	    first.next, first = second, first.next
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