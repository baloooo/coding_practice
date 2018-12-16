"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""
def add_two_numbsers_advanced(l1, l2):
    '''
    here l1 and l2 are given from msb and not lsb.
    Also you're not allowed to modify the list, i.e you cannot reverse l1 and l2

    Trick here is to use two stacks to get values of l1 and l2 and then pop elements from stack to construct
    the sum.
    https: // leetcode.com / problems / add - two - numbers - ii / discuss / 92623 / Easy - O(
        n) - Java - Solution - using - Stack
    '''
    pass

def add_two_numbers(l1, l2):
    # https://discuss.leetcode.com/topic/799/is-this-algorithm-optimal-or-what
    dummy = cur = ListNode('dummy')
    total_sum = 0
    # Base your logic on sum rather than individual nodes lists l1 and l2, it's more straightforward
    while l1 or l2:
        if l1:
            total_sum += l1.val
            l1 = l1.next
        if l2:
            total_sum += l2.val
            l2 = l2.next
        new_node = ListNode(total_sum % 10)
        cur.next = new_node
        cur = cur.next
        total_sum /= 10
    # if there is total sum remaining after both lists are done
    if total_sum:
        cur.next = ListNode(total_sum)
    return dummy.next

if __name__ == '__main__':
    lists = [[5, 8, 2], [4, 1, 5]]
    heads = []
    from linkedlistnode import construct_linked_list_from_array, ListNode
    for each in lists:
        heads.append(construct_linked_list_from_array(each))
    print add_two_numbers(heads[0], heads[1])
