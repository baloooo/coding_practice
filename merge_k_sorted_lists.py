from linkedlistbase import (
    construct_linked_list_from_array,
    ListNode, print_linked_list)
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        https://leetcode.com/problems/merge-k-sorted-lists/#/description
        :type lists: List[ListNode]
        :rtype: ListNode
        if there are k lists each with n elements. Total elements:nk
        Time: klogk (create min_heap) + (nk-k)2*logk (for popping and pushing elements)
        total: nklogk
        Space: O(k) for min_heap
        """
        from heapq import heappop, heapify, heapreplace
        min_heap = [(node.val, node) for node in lists if node]
        heapify(min_heap)
        head = cur_node = ListNode(0)
        while min_heap:
            val, node = min_heap[0]
            if node.next is None:
                heappop(min_heap)
            else:
                heapreplace(min_heap, (node.next.val, node.next))
            cur_node.next = node
            cur_node = cur_node.next
        return head.next

    def merge_two_linklist(head1, head2):
        cur = original = ListNode(None)
        while (head1 and head2):
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 or head2
        return original.next

    def merge_k_sorted_lists_optimized(sorted_ll_lists):
        # http://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
        # https://leetcode.com/articles/merge-k-sorted-list/
        # Notice that this tech. destroys the existing lists though which might
        # not be an acceptable strategy in some cases.
        # time: O(nlogk)
        # space: O(1)
        if not sorted_ll_lists:
            return None
        left = 0
        right = len(sorted_ll_lists) - 1
        while(right > 0):
            if left >= right:
                # when left crosses right re_initialize it to leftmost point
                left = 0
            sorted_ll_lists[left] = self.merge_two_linklist(sorted_ll_lists[left], sorted_ll_lists[right])
            left += 1
            right -= 1
        return sorted_ll_lists[0]


def merge_k_sorted_lists(list_head):
    original_head = merged_link_list = ListNode(None)
    while list_head:
        min_ll_head = min(list_head, key=lambda cur_head: cur_head.val)
        merged_link_list.next = min_ll_head
        merged_link_list = merged_link_list.next
        list_head.remove(min_ll_head)
        if min_ll_head.next is not None:
            list_head.append(min_ll_head.next)
    return original_head.next

if __name__ == '__main__':
    arr_list = [[10, 15, 25], [5, 12, 20], [1, 4, 7, 11, 17, 22]]
    # arr_list = []
    sorted_list = []
    for arr in arr_list:
        sorted_list.append(construct_linked_list_from_array(arr))
    # print_linked_list(merge_k_sorted_lists(sorted_list))
    # print_linked_list(merge_k_sorted_lists_using_heap(sorted_list))
    print_linked_list(merge_k_sorted_lists_optimized(sorted_list))
