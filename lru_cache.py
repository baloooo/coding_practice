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
Idea:

Make a Doubly LL where each node will store the value corresponding to a key.
This key: Node(val) mapping will be stored in a dictionary.
When a Get is issued for an existing key move it to end, else append new node at end
Gotchas:
Add node when no node present.
Add node when capacity is already full(pop node from head first)
Its always a good idea to modularize code as much as possible so when code base grows
its still manaegable, also you can get the zist of the logic just from method names.
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
    '''
    Have tried lot of combinations for modularizing code, this is the best I could find right now.
    '''
    def __init__(self, capacity):
        # {key: node_object}
        self.capacity = capacity
        self.list = DoublyLinkList()
        self.cache = {}

    def get(self, key):
        if self.cache.get(key):
            node = self.cache[key]
            self.list.move_to_end(node)
            return node.val
        else:
            return -1

    def set(self, key, value):
        if self.cache.get(key):
            # Just update the value on existing node
            val_node = self.cache[key]
            val_node.val = value
        else:
            if self.capacity != 0:
                self.capacity -= 1
            else:
                del self.cache[self.list.head.key]  # Delete head node from cache
                self.list.head = self.list.head.next  # map head to next head
                if self.list.head:
                    self.list.head.prev = None
                else:
                    self.list.last = None
            val_node = DoublyLinkListNode(key, value)
            self.cache[key] = val_node
        # Gotcha: udpate node order based on access time.
        if self.list.last:
            self.list.move_to_end(val_node)
        else:
            self.list.head = self.list.last = val_node

if __name__ == '__main__':
   capacity, inp = 2, 'S 2 1 S 1 1 S 2 3 S 4 1 G 1 G 2'
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

# 188ms LCode: Alternate implementation
import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = dict()
        self.dq = collections.deque()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.d: return -1
        self.dq.append(key)
        self.d[key][1] += 1
        return self.d[key][0]
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.dq.append(key)
        if not key in self.d:
            self.d[key] = [value,1]
        else:
            self.d[key][0] = value
            self.d[key][1] += 1
        if len(self.d) > self.capacity:
            while True:            
                k = self.dq.popleft()
                self.d[k][1] -= 1
                if self.d[k][1] == 0:
                    del self.d[k]
                    return
