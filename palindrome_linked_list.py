from math import ceil


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def construct_linked_list_from_array(inp_arr):
    head = Node(inp_arr[0])
    prev = head
    for each in inp_arr[1:]:
        node = Node(each)
        prev.next = node
        prev = node
    return head


def is_palindrome(head):
    list_len = 0
    original_head = base_ptr = head
    last_node = None

    while(head):
        list_len += 1
        if head.next is None:
            last_node = head
        head = head.next

    mid = int(ceil(list_len/2))
    for i in xrange(mid):
        base_ptr = base_ptr.next
    # reverse linklist from here
    next_ptr = old_next = base_ptr
    while(base_ptr is not None):
        if base_ptr.next is None:
            base_ptr.next = next_ptr
            break
        old_next = next_ptr
        next_ptr = base_ptr.next
        temp = next_ptr.next
        next_ptr.next = base_ptr
        base_ptr.next = old_next
        base_ptr = temp
    # traverse and match
    while(original_head != last_node):
        if original_head.val != last_node.val:
            break
        if original_head.next == last_node:
            return 1
        original_head = original_head.next
        last_node = last_node.next
    else:
        return 1
    return 0

if __name__ == '__main__':
    # inp_arr = [1, 2, 3, 4, 5]
    # inp_arr = [1, 2, 3, 2, 1]
    # inp_arr = [1, 2, 1]
    # inp_arr = [1, 1]
    # inp_arr = [1]
    # inp_arr = [1, 2, 3, 4, 4, 3, 2, 1]
    inp_arr = [4, 28, 6, 23, 46, 46, 23, 6, 28, 4]
    head = construct_linked_list_from_array(inp_arr)
    print is_palindrome(head)
