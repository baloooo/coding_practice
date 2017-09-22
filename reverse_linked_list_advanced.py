"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
"""

from linkedlistbase import (
    ListNode, construct_linked_list_from_array,
    print_linked_list)


def reverse_linked_list_with_params(head, m, n):
    cur = head
    last_unswapped_node = original_head = Node(-1)
    diff = n-m+1
    last_unswapped_node.next = cur
    # traverse till m
    while cur and m > 1:
        cur = cur.next
        last_unswapped_node = cur
        m -= 1
    prev = last_unswapped_node
    first_swapped_node = cur
    # swap from m to n
    while(cur and diff>1):
        cur.next = prev
        prev = cur
        cur = cur.next
        diff -= 1
    # link back nodes from n to end
    last_unswapped_node.next = prev
    first_swapped_node.next = cur
    return original_head.next


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

class Solution:
    def __init__(self):
        self.new_head = None

def reverse_linked_list_recursion(self, A):
    '''
    As recursion takes log(n) space so not space efficient.
    '''
    cur_node = A
    def reverse(cur_node):
        if cur_node.next is None:
            self.new_head = cur_node
            return cur_node
        next_node = reverse(cur_node.next)
        next_node.next = cur_node
        return cur_node
    last_node = reverse(cur_node)
    last_node.next = None
    return self.new_head



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
    # m = 4
    # n = 4
    # head = construct_linked_list_from_array(inp_arr)
    # print_linked_list(head)
    # print
    # print_linked_list(reverse_linked_list_with_params(head, m, n))
    # print_linked_list(reverse_linked_list(head))
    head = construct_linked_list_from_array(inp_arr)
    print_linked_list(head)
    print
    sol = Solution()
    print_linked_list(sol.reverse_linked_list_recursion(head))
