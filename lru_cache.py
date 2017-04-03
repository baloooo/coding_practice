# coding: utf-8
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.
get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least recently
used item before inserting the new item.
The LRUCache will be initialized with an integer corresponding to its capacity.
Capacity indicates the maximum number of unique keys it can hold at a time.

Definition of “least recently used” : An access to an item is defined as a
get or a set operation of the item. “Least recently used” item is the one
with the oldest access time.

NOTE: If you are using any global variables, make sure to clear them in
the constructor.
constructor.
Example :

Input :
         capacity = 2
         set(1, 10)
         set(5, 12)
         get(5)        returns 12
         get(1)        returns 10
         get(10)       returns -1
         set(6, 14)    this pushes out key = 5 as LRU is full.
         get(5)        returns -1

"""


class DoublyLinkListNode:
    def __repr__(self):
        return 'Key: {0}, Val: {1}'.format(self.key, self.val)

    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key


class DoublyLinkList:

    def __init__(self):
        self.head = None
        self.last = None

    def move_to_end(self, val_node):
        # val_node doesn't exist in list

        # if val_node is at last
        if self.last == val_node:
            return
        # val_node at beginning
        if val_node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            # val_node at between
            if val_node.prev:
                val_node.prev.next = val_node.next
                val_node.next.prev = val_node.prev
        # move val_node to end.
        self.last.next = val_node
        val_node.prev = self.last
        val_node.next = None
        self.last = val_node

    def delete(self, key, value):
        pass


class LRUCache:
    def __init__(self, capacity):
        # {key: node_object}
        self.capacity = capacity
        self.list = DoublyLinkList()
        self.cache = {}

    def get(self, key):
        # move this node to end
        try:
            val_node = self.cache[key]
        except KeyError:
            # todo: change it to int
            return -1
        self.list.move_to_end(val_node)
        return self.cache[key].val

    def set(self, key, value):
        if self.cache.get(key):
            self.cache[key].val = value
            val_node = self.cache[key]
        else:
            if self.capacity == 0:
                # Delete LRU (head node)
                del self.cache[self.list.head.key]
                self.list.head = self.list.head.next
                if self.list.head:
                    self.list.head.prev = None
                else:
                    self.list.last = None
            else:
                self.capacity -= 1
            # val_node = self.list.insert(key, value)
            val_node = DoublyLinkListNode(key, value)
            self.cache[key] = val_node
        # udpate node order based on access time.
        if self.list.last:
            self.list.move_to_end(val_node)
        else:
            self.list.head = self.list.last = val_node

if __name__ == '__main__':
    # capacity, inp = 11, 'S 1 1 G 11 G 11 S 3 10 G 10 S 3 12 S 1 15 S 4 12 G 15 S 8 6 S 5 3 G 2 G 12 G 10 S 11 5 G 7 S 5 1 S 15 5 G 2 S 13 8 G 3 S 14 2 S 12 11 S 7 10 S 5 4 G 9 G 2 S 13 5 S 10 14 S 9 11 G 5 S 13 11 S 8 12 G 10 S 5 12 G 8 G 11 G 8 S 9 11 S 10 6 S 7 12 S 1 7 G 10 G 9 G 15 G 15 G 3 S 15 4 G 10 G 14 G 10 G 12 G 12 S 14 7 G 11 S 9 10 S 6 12 S 14 11 G 3 S 7 5 S 1 14 S 2 8 S 11 12 S 8 4 G 3 S 13 15 S 1 4 S 5 3 G 3 G 9 G 14 G 9 S 13 10 G 14 S 3 9 G 8 S 3 5 S 6 4 S 10 3 S 11 13 G 8 G 4 S 2 11 G 2 G 9 S 15 1 G 9 S 7 8 S 4 3 G 3 G 1 S 8 4 G 13 S 1 2 G 3'  # noqa
    # capacity, inp = 2, 'S 2 1 S 1 1 S 2 3 S 4 1 G 1 G 2'
    capacity, inp = 11, 'S 1 1 G 11 G 11 S 3 10 G 10 S 3 12 S 1 15 S 4 12 G 15 S 8 6 S 5 3 G 2 G 12 G 10 S 11 5 G 7 S 5 1 S 15 5 G 2 S 13 8 G 3 S 14 2 S 12 11 S 7 10 S 5 4 G 9 G 2 S 13 5 S 10 14 S 9 11 G 5 S 13 11 S 8 12 G 10 S 5 12 G 8 G 11 G 8 S 9 11 S 10 6 S 7 12 S 1 7 G 10 G 9 G 15 G 15 G 3 S 15 4 G 10 G 14 G 10 G 12 G 12 S 14 7 G 11 S 9 10 S 6 12 S 14 11 G 3 S 7 5 S 1 14 S 2 8 S 11 12 S 8 4 G 3 S 13 15 S 1 4 S 5 3 G 3 G 9 G 14 G 9 S 13 10 G 14 S 3 9 G 8 S 3 5 S 6 4 S 10 3 S 11 13 G 8 G 4 S 2 11 G 2 G 9 S 15 1 G 9 S 7 8 S 4 3 G 3 G 1 S 8 4 G 13 S 1 2 G 3'  # noqa
    cache = LRUCache(capacity)
    index = 0
    inp_arr = inp.split(' ')
    out = '-1 -1 -1 -1 -1 -1 -1 -1 -1 12 -1 -1 4 14 12 5 12 6 11 -1 -1 12 6 -1 6 11 11 5 12 12 12 10 11 10 11 4 4 -1 11 10 10 5 -1 -1 5'.split(' ')  # noqa
    out_index = 0
    while index < len(inp_arr):
        # print cache.cache
        op = inp_arr[index]
        if op == 'S':
            key, value = inp_arr[index+1], inp_arr[index+2]
            cache.set(key, value)
            print 'SET %s: %s' % (key, value)
            index += 3
        else:
            if cache.get(inp_arr[index+1]) == out[out_index]:
                print "passed: OP: GET {0}".format(inp_arr[index+1])
            else:
                print "failed: expected: {0}, got: {1}".format(
                    out[out_index], cache.get(inp_arr[index+1]))
            index += 2
            out_index += 1
