from linkedlistbase import Node, construct_linked_list_from_array, print_linked_list
from time import sleep

"""
new implementation
Idea: https://discuss.leetcode.com/topic/18100/java-merge-sort-solution
Basically combination of:
    a. Find mid
    b. merge two sorted linked lists
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, l1, l2):
        dummy = cur = ListNode('dummy')
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next

    def get_mid(self, head):
        slow = fast = first_half_tail = head
        while fast and fast.next:
            first_half_tail = slow
            slow = slow.next
            fast = fast.next.next
        # split LL in two halves.
        first_half_tail.next = None
        return slow
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Idea: MergeSort
        """
        # Base condition (No two nodes swapping in LL)
        if head is None or head.next is None:
            return head
        # gets mid also splits LL in two halves
        mid = self.get_mid(head)
        l1 = self.sortList(head)
        l2 = self.sortList(mid)
        return self.merge(l1, l2)


def find_mid(head, last):
    tor = hare = head
    while(hare != last and hare.next is not None and hare.next.next is not None):
        tor = tor.next
        hare = hare.next.next
    return tor

def merge(lo, hi):
    original_head = new_head = Node(-1)
    while(lo is not None and hi is not None):
        if lo.val<hi.val:
            original_head.next = lo
            original_head = original_head.next
            lo = lo.next
        else:
            original_head.next = hi
            original_head = original_head.next
            hi = hi.next
    while(lo is not None):
        original_head.next = lo
        lo = lo.next
        original_head = original_head.next
    while(hi is not None):
        original_head.next = hi
        hi = hi.next
        original_head = original_head.next
    original_head.next = None
    return new_head.next

def msort(head, last):
    if head == last:
        return head
    mid = find_mid(head, last)
    part2_start = mid.next
    mid.next = None
    if head != mid:
        lo = msort(head, mid)
    else:
        lo = head
        lo.next = None
    if part2_start != last:
        hi = msort(part2_start, last)
    else:
        hi = part2_start
        hi.next = None
    return merge(lo, hi)

if __name__ == '__main__':
    arr = [5, 3, 2, 10, 1]
    arr = [5, 4, 3, 2, 1]
    arr = [1, 1, 1, 1]
    arr = [1]
    arr = [2, 1]
    head = construct_linked_list_from_array(arr)
    tmp = head
    while(tmp.next is not None):
        tmp=tmp.next
    new_head = msort(head, tmp)
    print_linked_list(new_head)
