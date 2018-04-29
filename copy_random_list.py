class Solution(object):
    def copyRandomList_basic(self, head):
        """
        Idea is to create a mapping of original node -> copied node while taking care of
        the fact that next and random nodes may or may not be already present in the node_map.

        https://discuss.leetcode.com/topic/9557/clear-and-short-python-o-2n-and-o-n-solution/6
        Time: O(n) Space: O(n), space is due to the node_map dictionary
        """
        node_map = collections.defaultdict(lambda : RandomListNode(0))
        cur = head
        node_map[None] = None
        while cur:
            node_map[cur].label = cur.label
            node_map[cur].next = node_map[cur.next]
            node_map[cur].random = node_map[cur.random]
            cur = cur.next
        return node_map[head]

    def copyRandomList_optimized(self, head):
        """
        Time: O(n) Space: O(1)
        Idea: 
        The idea is to associate the original node with its copy node in a single linked list.
        In this way, we don’t need extra space to keep track of the new nodes.

        The algorithm is composed of the follow three steps which are also 3 iteration rounds.

        * Iterate the original list and duplicate each node. The duplicate
            of each node follows its original immediately.
        * Iterate the new list and assign the random pointer for each
            duplicated node.
        * Restore the original list and extract the duplicated nodes.

        https://discuss.leetcode.com/topic/7594/a-solution-with-constant-space-complexity-o-1-and-linear-time-complexity-o-n
        """
        if not head:
            return
        # Insert copies in original linkedlist
        orig_head = head
        while head:
            copy = RandomListNode(head.label)
            temp = head.next
            head.next = copy
            copy.next = temp
            head = temp
        # Set random links on copy nodes
        head = orig_head
        while head:
            if head.random is not None:
                head.next.random = head.random.next
            head = head.next.next
        # seggregate original and copy linkedlists
        head = orig_head
        orig_head = cur = RandomListNode('-1')
        while head:
            cur.next = head.next
            head.next = head.next.next
            head = head.next
            cur = cur.next
        cur.next = None
        return orig_head.next

    def copyRandomList_optimized2(self, head):
		'''
		similar to above just using single line assignments to prevent using temp variables
		'''
        # place copies of existing nodes.
        cur = head
        while cur:
            copy = RandomListNode(cur.label)
            cur.next, copy.next = copy, cur.next
            cur = cur.next.next
        # create random pointers.
        cur = head
        new_head = cur.next
        while cur:
            cur.next.random = cur.random.next if cur.random else None # This part is tricky in case of one node
            cur = cur.next.next
        # seggregate original and copied lists.
        cur = head
        copy_cur = head.next
        while cur:
            cur.next = copy_cur.next
            copy_cur.next = cur.next.next if cur.next else None # This part is tricky in case of one node

            cur = cur.next
            copy_cur = copy_cur.next
        return new_head


    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        Idea: https://discuss.leetcode.com/topic/9557/clear-and-short-python-o-2n-and-o-n-solution/6
        Time: O(n) space: O(n)
        """
        if not head:
            return
        nodes_map = {}
        base = head
        while base:
            nodes_map[base] = RandomListNode(base.label)
            base = base.next
        base = head
        while base:
            nodes_map[base].next = nodes_map.get(base.next)
            nodes_map[base].random = nodes_map.get(base.random)
            base = base.next
        return nodes_map[head]

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        cur = head
        # First round: make copy of each node, and link them together side-by-side in a single list.
        while cur:
            copy = RandomListNode(cur.label)
            cur.next, copy.next = copy, cur.next
            cur = cur.next.next
        # Second round: assign random pointers for the copy nodes. Link copied nodes
        cur = head
        while cur:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # Third round: restore the original list, and extract the copy list. seggregate orig and copied nodes
        orig_iter = head
        copy_head = copy = RandomListNode(-1)
        while orig_iter:
            orig_next = orig_iter.next.next
            
            # extract the copy
            copy.next = orig_iter.next
            copy = copy.next
            
            # restore the original list
            orig_iter.next = orig_next
            
            orig_iter = orig_next
        return copy_head.next

