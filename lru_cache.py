# coding: utf-8
"""
Todo:
    Get Time and Space complexities and other pros and cons for both the approaches.
    Support:
        multithreading/multiprocessing
        Distributed cache


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

"""
Idea 1:

We need a Doubly LL b'coz given just head and tail of a linked list, to 
remove a node or move a node to end would require O(n) time.
Make a Doubly LL where each node will store the value corresponding to a key.
This key: Node(val) mapping will be stored in a dictionary.
When a Get is issued for an existing key move it to end, else append new node at end
Gotchas:
Add node when no node present.
Add node when capacity is already full(pop node from head first)
Its always a good idea to modularize code as much as possible so when code base grows
its still manaegable, also you can get the zist of the logic just from method names.

Time: 
Space: 
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
    '''
    Simulates a standard Queue where oldest person in the line is the at the Front,
    and Back has the person that just came in. Back ---> Front
    '''

    def __init__(self):
        self.head = None
        self.last = None

    def move_to_end(self, val_node):
        # val_node doesn't exist in queue

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

    def delete(self, node=None):
        if node is None:
            # Delete node from head, and readjust head
            self.queue.head = self.queue.head.next  # map head to next head
            if self.queue.head:
                self.queue.head.prev = None
            else:
                self.queue.last = None
        else:
            # Todo: Delete keys from cache
            pass

    def add(self, key, val):
        node = DoublyLinkListNode(key, value)
        return node


class LRUCache:
    '''
    Have tried lot of combinations for modularizing code, this is the best I could find right now.
    Notice that once queue tops up, only one node is deleted to fit an insertion. nodes are not 
    deleted automotically.
    '''
    def __init__(self, capacity):
        # {key: node_object}
        self.capacity = capacity
        self.queue = DoublyLinkList()
        self.cache = {}

    def get(self, key):
        if self.cache.get(key):
            node = self.cache[key]
            self.queue.move_to_end(node)
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
                del self.cache[self.queue.head.key]  # Delete head node from cache
                self.queue.delete()
            self.cache[key] = self.queue.add(key, value)
        # Gotcha: udpate node order based on access time.
        # If cache is not Empty
        if self.queue.last:
            self.queue.move_to_end(val_node)
        else:
            self.queue.head = self.queue.last = val_node


*********************************************************************************************************
Slightly alternate implementation of the same Idea 1 with may be less variable movements.

class DLLNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class DLL(object):
    def __init__(self):
        self.front = None
        self.tail = None
    
    def move_to_front(self, node):
        # node is already in front, notice this will also be true if there is only one node and tail and front are one node.
        if node == self.front:
            return
        # node is in tail
        elif node == self.tail:
            self.tail = self.tail.next
        # node is in middle
        else:
            node.prev.next, node.next.prev = node.next, node.prev

        # append node in front
        self.front.next = node
        node.prev = self.front
        node.next = None
        self.front = self.front.next
        
    
    def pop(self):
        # delete rear node
        self.tail = self.tail.next
    
    def append(self, key, val):
        # Add new key,val node to front.
        node = DLLNode(key, val)
        if self.front is None:
            self.front = self.tail = node
        else:
            self.front.next = node
            node.prev = self.front
            node.next = None
            self.front = self.front.next
        return node
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.queue = DLL()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            self.queue.move_to_front(self.cache[key])
        return self.cache[key].val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache[key].val = value
            self.queue.move_to_front(self.cache[key])
            return
        elif self.capacity == 0:
            del self.cache[self.queue.tail.key]
            self.queue.pop()
        else:
            self.capacity -= 1
        # handle empty queue and other border conditions
        node = self.queue.append(key, value)
        self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
*********************************************************************************************************

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


class LRUCache_naive(object):
	'''
	Idea 2: Use DEQUE (storing just keys) along with hash map for key: val mappings
	'''

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.q = collections.deque()
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
		Time: O(n) since removing an ele from deque requires O(n), this is improved in Idea 1 where
		reference to DLL nodes are stored instead in cache thereby allowing O(1) removal of nodes.
        """
        if key not in self.cache:
            return -1
        # remove and add it just so as to place this key in the very rear of queue(DLL) so as to prevent it's eviction.
        self.q.remove(key)
        self.q.append(key)
        return self.cache[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
		O(n) since if key is already in cache updation would require deleting key from deque
		which is a O(n) operation
        """
        if key in self.cache:
            self.q.remove(key)
        elif len(self.cache) == self.capacity:
            remove_key = self.q.popleft()
            del self.cache[remove_key]
            
        self.q.append(key)
        self.cache[key] = value
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# 188ms LCode: Alternate implementation
class LRUCache(object):

    '''
    Idea 3:
    This is actually a bad idea, Idea 2 is similar to this and a better version of this so this
    should never be used. This is kept just for logging purposes
    The idea is to store a tuple (key, val, access_time) in queue and for every access
    add a new entry to queue with updated access time (when capacity is reached old (k,v,a_time)
    tuple will be flushed out by delete_old_entries method
    Cons:
        Storage of stale (key,value,access_time) tuples in queue for maintaining LRU contract,
        though dictionary self.cache will always have latest values.
    '''

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from Queue import deque
        self.capacity = capacity
        self.queue = deque()  # Back --> Front
        self.time_stamp = 0
        self.cache = {}

    def delete_old_entries(self):
        while len(self.cache) > self.capacity: # more entries in cache than the capacity
            key, value, time = self.queue.pop()  # pop the front of the queue
            value_from_cache, time_from_cache = self.cache[key]
            '''
            Pop this entry from cache also since access time and value matches with cache entries,
            this is done b'coz value for a key can be updated and hence the access time in which case
            only the entry from queue should be removed not from the cache.
            '''
            if value == value_from_cache and time == time_from_cache:
                del self.cache[key]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        Time: O(1)
        since get only changes access times which would only change which entry would
        be evicted in case someone now try to add an entry, we don't need to call delete_old_entries
        since the count of entries is still the same.
        """
        try:
            value, _ = self.cache[key]
        except KeyError:
            return -1
        self.time_stamp += 1
        self.cache[key] = (value, self.time_stamp)
        self.queue.appendleft((key, value, self.time_stamp))
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        Time: O(n), n being total number of get operations. As each new get(x) will generate a new
        tuple which will not be flushed out untill first put operation.
        """
        self.time_stamp += 1
        self.cache[key] = (value, self.time_stamp)
        self.queue.appendleft((key, value, self.time_stamp))
        self.delete_old_entries()
