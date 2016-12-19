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


def merge_two_sorted(head1, head2):
    original_head_backup = original_head = Node(0)
    while(head1 is not None and head2 is not None):
        if head1.val < head2.val:
            original_head.next = head1
            head1 = head1.next
        else:
            original_head.next = head2
            head2 = head2.next
        original_head = original_head.next
    if head1 is not None:
        original_head.next = head1
    if head2 is not None:
        original_head.next = head2
    return original_head_backup

if __name__ == '__main__':
    # lists = [[5, 8, 20], [4, 11, 15]]
    lists = [[], []]
    heads = []
    for each in lists:
        heads.append(construct_linked_list_from_array(each))
    new_head = merge_two_sorted(heads[0], heads[1])
    print_linked_list(new_head.next)
