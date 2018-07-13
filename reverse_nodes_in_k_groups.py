"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Idea:
	Step1: verify if k nodes exist, and get a pointer to next group's head in the same loop.
	Step2: reverse k nodes
	Step3: link head of this group to next group and tail of this group to head of prev group
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

	def get_len(self, head):
		count = 0
		while head:
			head = head.next
			count += 1
		return count

    def reverseKGroup_2(self, head, k):
        """
		More optimized than _1 since we don't have to do step 1
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        Step1: Get len of LL
        Step 2: Reverse group of k nodes
        Step 3: cur_head.next, prev_grp_head.next = cur, prev
        """
        if head is None or head.next is None: return head
        n = self.get_len(head)
        if k > n: return head
        rep = n / k # Notice this makes sure we only run the loop when we have k nodes to reverse
        orig_head = prev_grp_head = ListNode(-1)
        cur_head = head
        while rep > 0:
        	# Reverse k nodes
        	prev, cur = None, cur_head
        	count = 0
        	while count < k:
        		next = cur.next
        		cur.next = prev
        		prev = cur
        		cur = next
        		count += 1
        	# Stich prev head with reversed list's head.
        	cur_head.next, prev_grp_head.next = cur, prev
			# Readjust pointers for next iteration
        	cur_head, prev_grp_head = cur, cur_head
        	rep -= 1

        return orig_head.next


class Solution(object):
	def reverseKGroup_1(self, head, k):
        if not head or not head.next: return head
        orig_head = prev_grp_head = ListNode('dummy')
        orig_head.next = nxt_grp_head =  head
        while nxt_grp_head:
			# Step1
            # Traverse k node ahead, to check if k nodes available and place the pointer at next group head.
            for _ in xrange(k):
                if nxt_grp_head is not None:
                    nxt_grp_head = nxt_grp_head.next
                else:
                    break
			# Step2
            # reverse current group
			'''Notice that prev is set to nxt_grp_head cleverly to deal with situations where
			k is not an integral multiple of length of the LL. In that situation we've already
			linked the tail of current grp to head of remaining part of the LL sucessfully,
			and therefore we an return directly whenever traverse k nodes above exits prematurely.'''
            prev, cur, next_p = nxt_grp_head, head, None
            while cur != nxt_grp_head:
                next_p = cur.next
                cur.next = prev
                prev = cur
                cur = next_p
			# Step3
            # Link cur group with previous group and move to next group
            prev_grp_head.next = prev # prev variable is on tail of cur_group
            prev_grp_head = head # move head is on cur grp's head, so advancing prev_grp_head accordingly
            head = nxt_grp_head # move head to next grp head
        return orig_head.next

    def reverseKGroup(self, head, k):
        """
        verify if k nodes exist, and get a pointer to next group's head in the same loop.i
        reverse k nodes
        link head of this group to next group and tail of this group to head of prev group
        """
        prev_tail = dummy = ListNode('dummy')
        # l and r are the limits in which nodes need to be reversed
        prev_tail.next = l = r = head
        count = 0
        while True:
            # Move r one step over, so as to land it on the next node of k group nodes which then can be used to connect prev grp
            while count < k and r:
                r = r.next
                count += 1
            if count == k:
                # reverse k nodes
                # set pre to next groups head node, which is intentionally where r is sitting.
                pre, cur = r, l
                while count > 0:
                    next = cur.next
                    cur.next = pre # (1)
                    pre = cur
                    cur = next
                    count -= 1
            #set prev_tail.next to pre which is joining prev tail to currently reversed group head
            #set prev_tail to l to point it now at the previous goups tail
            #(notice l points to tail now since this group is now reversed)
            #set r to l this will be the pre or head of prev reversed group which will
            #be set to next groups tail in (1)
            # This is the most imp. part of the exercise
                prev_tail.next, prev_tail, l = pre, l, r
            else:
                return dummy.next

if __name__ == '__main__':
    from linkedlistbase import construct_linked_list_from_array
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    head, k = construct_linked_list_from_array(arr), 3
    Solution().reverseKGroup(head, k)
