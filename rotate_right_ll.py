from linkedlistbase import construct_linked_list_from_array, print_linked_list


class Solution(object):
    def rotateRight(self, head, k):
        """
        Given a linked list, rotate the list to the right by k places, where k is non-negative.

        Example 1:

        Input: 1->2->3->4->5->NULL, k = 2
        Output: 4->5->1->2->3->NULL
        Explanation:
        rotate 1 steps to the right: 5->1->2->3->4->NULL
        rotate 2 steps to the right: 4->5->1->2->3->NULL
        Example 2:

        Input: 0->1->2->NULL, k = 4
        Output: 2->0->1->NULL
        Explanation:
        rotate 1 steps to the right: 2->0->1->NULL
        rotate 2 steps to the right: 1->2->0->NULL
        rotate 3 steps to the right: 0->1->2->NULL
        rotate 4 steps to the right: 2->0->1->NULL
        Idea:https://discuss.leetcode.com/topic/14470/my-clean-c-code-quite-standard-find-tail-and-reconnect-the-list/22
        """
        if not head or not k or not head.next:
            return head
        # get LL length
        len = 1
        orig_head = head
        while head.next is not None:
            head = head.next
            len += 1
        head.next = orig_head # circle the LL
        k = k % len
        head = orig_head
        for _ in xrange(len-k-1): # when the head is at len-k-1 node(i.e just before our end node)
            head = head.next
        orig_head = head.next
        head.next = None
        return orig_head

if __name__ == '__main__':
    arr, r = [1, 2], 1
    head = construct_linked_list_from_array(arr)
    print_linked_list(head)
    print
    new_head = Solution().rotateRight(head, r)
    print_linked_list(new_head)
