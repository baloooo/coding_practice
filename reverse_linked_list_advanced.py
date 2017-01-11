"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
"""

from linkedlistbase import (
    Node, construct_linked_list_from_array,
    print_linked_list)


def reverse_linked_list_with_params(A, m, n):
    original_head = head = A
    for i in xrange(1, m-1):
        head = head.next
    lower_half = head
    if lower_half.next is None:
        return lower_half
    print 'lower half starts here', head.val
    last = None
    cur = head
    nxt = reverse_pipe_end_node = cur.next
    print 'm: %d, n: %d' % (m, n)
    # for i in xrange(m, n+2):
    i = m
    while(i <= n):
        print 'i: ', i
        nxt = cur.next
        cur.next = last
        last = cur
        cur = nxt
        i += 1
    reverse_pipe_end_node.next = cur
    lower_half.next = last
    return original_head


def reverse_linked_list_optimized(A):
    # Most optimized solution
    last = None
    cur = A
    nxt = A.next
    while cur is not None:
        nxt = cur.next
        cur.next = last
        last = cur
        cur = nxt
    return last


def reverse_linked_list(head):
    # First shot at reversing linked list
    # node for 1 and 2 nodes
    if head.next is None:
        return head
    if head.next.next is None:
        new_head = head.next
        new_head.next = head
        head.next = None
        return new_head
    # code for greater than 2 nodes
    current_node = head
    next_node = None
    while((current_node.next is not None) and
          (current_node.next.next is not None)):
        jump_node = current_node.next.next
        next_node_backup = next_node
        next_node = current_node.next
        current_node.next = next_node_backup
        next_node.next = current_node
        current_node = jump_node
    if current_node.next is None:
        current_node.next = next_node
        new_head = current_node
    elif current_node.next.next is None:
        next_node_backup = next_node
        next_node = current_node.next
        current_node.next = next_node_backup
        next_node.next = current_node
        new_head = next_node
    return new_head


if __name__ == '__main__':
    inp_arr = [1, 2, 3, 4]
    # inp_arr = [1, 2, 3, 4, 5, 6]
    # inp_arr = [1]
    # inp_arr = [1, 2]
    # inp_arr = [1, 2, 3]
    m = 1
    n = 4
    head = construct_linked_list_from_array(inp_arr)
    print_linked_list(head)
    print
    print_linked_list(reverse_linked_list_with_params(head, m, n))
    # print_linked_list(reverse_linked_list(head))
