from linkedlistbase import Node, construct_linked_list_from_array, print_linked_list
from time import sleep

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
