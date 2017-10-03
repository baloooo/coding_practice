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

def reverse(self, head, orig_last):
    last, cur, next = None, head, head.next
    while cur is not orig_last:
        next = cur.next
        cur.next = last
        last = cur
        cur = next
    return last


def find_mid(self, head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def is_palindrome_optimized(self, head):
    # This kind of approach is better for understanding.
    mid = self.find_mid(head)
    self.reverse(head, mid)
    cur = mid
    while head != mid or cur is not None:
        if head.val != cur.val:
            return False
        head = head.next
        cur = cur.next
    return True

def is_palindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    orig_head = head
    pre, next = None, None
    slow = fast = head
    # Find mid and reverse first half together
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        next = head.next
        head.next = pre
        pre = head
        head = next
    orig_head = pre
    # slow should be at half way point
    if fast is not None:
        slow = slow.next
    # Match both halves of the LL
    while slow:
        if orig_head.val != slow.val:
            return False
        slow = slow.next
        orig_head = orig_head.next
    return True


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], False),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 1], True),
        ([1, 1], True),
        ([1], True),
        ([1, 2, 3, 4, 4, 3, 2, 1], True),
        ([4, 28, 6, 23, 46, 46, 23, 6, 28, 4], True),
    ]
    for test_case in test_cases:
        head = construct_linked_list_from_array(test_case[0])
        res = is_palindrome(head)
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
