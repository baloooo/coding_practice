"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        https://discuss.leetcode.com/topic/7005/very-concise-one-pass-solution/20
        The idea is to just iterate over all the nodes and move nodes
        less than x to first_half list and others to second_half list. In the end
        join first_half end to second_half start and nullify second_half end
        """
        first_half = start = ListNode('first_half')
        second_half = second_start = ListNode('second_half')
        while head:
            if head.val < x:
                first_half.next = head
                first_half = first_half.next
            else:
                second_half.next = head
                second_half = second_half.next
            head = head.next
        first_half.next = second_start.next
        # Note: Close the second half. This is imp. since existing links can cause infinite loops
        second_half.next = None
        return start.next

if __name__ == '__main__':
    arr, x = [2, 1], 2
    from linkedlistbase import construct_linked_list_from_array, print_linked_list
    head = construct_linked_list_from_array(arr)
    res = Solution().partition(head, x)
    print_linked_list(res)
