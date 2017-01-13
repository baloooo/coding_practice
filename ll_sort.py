"""
Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5
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


def qsort(head):
    pass

if __name__ == '__main__':
    arr = [1, 5, 4, 3]
    head = construct_linked_list_from_array(arr)
    head = qsort(head)
    print_linked_list(head)
