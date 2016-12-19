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


def add_two_numbers(head1, head2):
    original_head = head = Node(-1)
    carry = 0
    while(head1 is not None and head2 is not None):
        digit_sum = head1.val + head2.val
        if carry:
            digit_sum += carry
        if digit_sum > 9:
            carry = digit_sum/10
            digit_sum = digit_sum % 10
        new_node = Node(digit_sum)
        head.next = new_node
        head = head.next
    if carry:
        new_node = Node(carry)
        head.next = new_node
        head = head.next
    return original_head


if __name__ == '__main__':
    lists = [[5, 8, 2], [4, 1, 5]]
    heads = []
    for each in lists:
        heads.append(construct_linked_list_from_array(each))
    print add_two_numbers(heads[0], heads[1])
