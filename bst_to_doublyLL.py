class DoublyLL:
    def __init__(self, data):
        self.data = data
        # By default single node will be circular
        self.prev = None
        self.next = None


class Solution:
    def __init__(self):
        pass

    def traverse(self, root):
        """
        class DoublyLL:
            def __init__(self):
                self.data = None
                self.prev = None
                self.next = None
        """
        # Typical Inorder traversal
        if root is None:
            return
        self.traverse(root.left)
        if self.prev:
            self.prev.right = self.head
        else:
            self.orig_head = self.head

        self.head.data = root.data
        self.head.prev = self.prev
        self.prev = self.head
        self.head = DoublyLL()
        self.traverse(root.right)

    def append(self, first_ll, second_ll):
        """
        http://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/
        Appends second_ll to the end of first_ll and adds the circular connection
        from tail of second_ll to head of first_ll
        """
        first_head = first_ll
        second_head = second_ll
        if first_ll is None:
            return second_ll
        if second_ll is None:
            return first_ll
        first_ll.prev.next = second_ll
        temp = second_ll.prev
        second_ll.prev = first_ll.prev
        first_ll.prev = temp
        temp.next = first_ll
        return first_ll

    def tree_to_ll(self, root):
        """
        Alternate method:
        http://cslibrary.stanford.edu/109/TreeListRecursion.html
        The neat thing about this idea is that, it breaks down this process
        to very rudimentary blocks which allows us to have more granular control
        over the doubly linked list creation. For ex: we can also generate linkedlist from
        zig-zag traversal of tree using this approach.
        class DoublyLL:
            def __init__(self, data):
                self.data = data
                # By default single node will be circular
                self.prev = self
                self.next = self
        """
        if root is None:
            return
        left = self.tree_to_ll(root.left)
        right = self.tree_to_ll(root.right)
        cur = DoublyLL(root.val)
        cur.prev = cur.next = cur
        left = self.append(left, cur)
        left = self.append(left, right)
        return left


if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    test_cases = [
        ('test1', 'sol1'),
    ]
    arr = [100, 50, 150, 25, 75, 125, 175]
    root = level_order_array_to_tree(arr)
    head = Solution().tree_to_ll(root)
    i = 0
    while i < 7:
        print head.data
        i += 1
        head = head.next
