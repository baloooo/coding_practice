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
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key


class LRUCache:
    def __init__(self, capacity):
        # {key: node_object}
        self.capacity = capacity
        self.cur_capacity = 0
        self.cache = {}
        self.head = None
        self.last = None

    def get(self, key):
        # move this node to end
        try:
            val_node = self.cache[key][0]
        except KeyError:
            return -1
        if val_node != self.last:
            if val_node == self.head:
                self.head = val_node.next
                self.head.prev = None
            else:
                val_node.prev.next = val_node.next
            self.last.next = val_node
            val_node.prev = self.last
            val_node.next = None
            self.last = val_node
        return self.cache[key][1]

    def set(self, key, value):
        # update on same key should just change value not create entire new
        if self.cur_capacity == self.capacity:
            # Delete LRU (head node)
            del self.cache[self.head.key]
            self.head = self.head.next
            self.head.prev = None
        val_node = DoublyLinkListNode(key, value)
        if self.last:
            self.last.next = val_node
            val_node.prev = self.last
            self.last = val_node
        else:
            self.head = self.last = val_node
        self.cache[key] = (val_node, value)
        self.cur_capacity += 1

if __name__ == '__main__':
    capacity = 2
    cache = LRUCache(capacity)
    cache.set(1, 10)
    cache.set(5, 12)
    print cache.get(5)
    print cache.get(1)
    print cache.get(10)
    cache.set(6, 14)
    print cache.get(5)
    # check when capacity is 1
