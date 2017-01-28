from linkedlistbase import (
    construct_linked_list_from_array,
    ListNode, print_linked_list)
import heapq

# http://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
# time: O(nlogk)
# space: O(1)


def merge_k_sorted_lists_optimized(sorted_ll_lists):
    def merge_two_linklist(head1, head2):
        # alternate approach if no Node method is available
        # if head1 is None or head2 is None:
        #     return head1 or head2
        # if head1.val > head2.val:
        #     head1, head2 = head2, head1
        # original = head1
        # while head1.next is not None:
        #     if head2.val < head1.next.val:
        #         temp = head1.next
        #         head1.next = head2
        #         head2 = temp
        #     head1 = head1.next
        # return original
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
    if not sorted_ll_lists:
        return None
    left = 0
    right = len(sorted_ll_lists) - 1
    while(right > 0):
        if left >= right:
            # when left crosses right re_initialize it to leftmost point
            left = 0
        sorted_ll_lists[left] = merge_two_linklist(
            sorted_ll_lists[left], sorted_ll_lists[right])
        left += 1
        right -= 1
    return sorted_ll_lists[0]


# Time: O(nlogk) ( n being total nodes cumulative of k lists)
# space: O(k) (for min heap)
def merge_k_sorted_lists_using_heap(sorted_ll_list):
    min_heap = []
    original_head = merged_link_list = ListNode(None)
    # Can be optimized from O(klogk) to O(k) if we gather all list items in
    # heap and heapify once rather than executing heappush k times.
    for list_head in sorted_ll_list:
        heapq.heappush(min_heap, (list_head.val, list_head))
    # loop
    while(min_heap):
        heap_min = heapq.heappop(min_heap)
        merged_link_list.next = heap_min[1]
        merged_link_list = merged_link_list.next
        if heap_min[1].next is not None:
            heapq.heappush(min_heap, (heap_min[1].next.val, heap_min[1].next))
    return original_head.next


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
