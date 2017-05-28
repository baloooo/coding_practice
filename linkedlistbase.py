class ListNode(object):
    def __str__(self):
        return "linkedlist node_val is %s" % self.val

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def construct_linked_list_from_array(inp_arr):
    if not inp_arr:
        return
    head = ListNode(inp_arr[0])
    prev = head
    for each in inp_arr[1:]:
        node = ListNode(each)
        prev.next = node
        prev = node
    return head


def print_linked_list(head):
    while(head):
        print head.val,
        head = head.next
