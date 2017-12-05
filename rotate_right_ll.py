from linkedlistbase import construct_linked_list_from_array, print_linked_list


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
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
