"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input :

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3.
"""
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


def get_head_node_for_cycle(head):
    # Note: fast and slow both start at head not ahead of each other
    fast = slow = head
    while(fast and fast.next):
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            fast = head
            while(fast!=slow):
                fast = fast.next
                slow = slow.next
            return slow.val

if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = construct_linked_list_from_array(nodes)
    last_node = cycle_head = head
    while(last_node.next is not None):
        last_node = last_node.next
    for i in xrange(3):
        cycle_head = cycle_head.next
    print "last node is %d and cycle head is %d" % (last_node.val, cycle_head.val)
    last_node.next = cycle_head
    print get_head_node_for_cycle(head)
