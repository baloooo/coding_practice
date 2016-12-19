class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def construct_linked_list_from_array(inp_arr):
    if not inp_arr:
        return
    head = Node(inp_arr[0])
    prev = head
    for each in inp_arr[1:]:
        node = Node(each)
        prev.next = node
        prev = node
    return head


def print_linked_list(head):
    while(head):
        print head.val,
        head = head.next

def reverse_linked_list_with_params(A, m, n):
    temp_head = A
    linked_list_length = 0
    while(temp_head.next is not None):
        linked_list_length+=1

    if 1<m<n<linked_list_length:

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
    while((current_node.next is not None) and (current_node.next.next is not None)):
        jump_node = current_node.next.next
        next_node_backup = next_node
        next_node = current_node.next
        current_node.next = next_node_backup
        next_node.next = current_node
        current_node = jump_node
    # import ipdb; ipdb.set_trace()
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
    # inp_arr = [1, 2, 3, 4, 5]
    # inp_arr = [1, 2, 3, 4, 5, 6]
    # inp_arr = [1]
    inp_arr = [1, 2]
    head = construct_linked_list_from_array(inp_arr)
    print_linked_list(head)
    print 
    print_linked_list(reverse_linked_list(head))