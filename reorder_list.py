# coding: utf-8
"""
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' vals.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

from linkedlistbase import construct_linked_list_from_array


class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def list_pivoting(self, head, k):
        # TODO - you fill in here.
        '''
        10, 50, 20, 100, 150, 5, 7, 11, 190
        k = 50
        10, 50, 20, 5, 7, 11, 100, 150, 190
        '''
        if head is None or head.next is None:
            return head
        less_than_k = orig_less_than_k = ListNode(None, None)
        greaeter_than_k = orig_greater_than_k = ListNode(None, None)
        print('K: ', k)
        while head:
            print(head.val)
            if head.val < k:
                less_than_k.next = head
                less_than_k = less_than_k.next
                head = head.next
                less_than_k.next = None
            else:
                greaeter_than_k.next = head
                greaeter_than_k = greaeter_than_k.next
                head = head.next
                greaeter_than_k.next = None
        less_than_k.next = orig_greater_than_k.next

        head = orig_less_than_k.next
        print('printing list')
        while head is None:
            print(head.val)
        return orig_less_than_k.next


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
    arr = [-8, -2, -7, 4, 17, 16, 15, 6, -3, 8, 13, -11, 9, 22, 2, 3, -4, 11, 1, -5, -9, 21, 14, 19, 7, 18, 20, 5, -1, 0, 12, -6, 23, -10, -12, 10]
    head = construct_linked_list_from_array(arr)
    res = Solution().list_pivoting(head, 3)
    print 'res is ', res
    # for index, test_case in enumerate(test_cases, 1):
    #     head = construct_linked_list_from_array(test_case[0])
    #     res = Solution().reorder_list(head)
    #     expected_res = construct_linked_list_from_array(test_case[1])
    #     if compare_two_linked_lists(res, expected_res):
    #         print "%d: Passed" % index
    #     else:
    #         print "%d: Failed" % index
