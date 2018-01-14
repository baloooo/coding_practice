'''
23 / 23 test cases passed.
Status: Accepted
Runtime: 255 ms
'''
from collections import defaultdict

class DoublyLLNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

    def __repr__(self):
        return 'Key: %s, val: %s, freq: %s' % (self.key, self.val, self.freq)

class DoublyLinkedList(object):
    def __init__(self):
        # We'll be adding nodes on tail and deleting nodes from head
        # This will ensure that for LinkedList nodes of same frequency
        # we delete node which was least recently used, in other words
        # fall back strategy for LFU (if there're multiple nodes with least freq)
        # delete node which was used least recently
        self.head = None
        self.tail = None

    def append(self, node):
        node.next, node.prev = None, None # Avoid dirty reads
        if self.head is None:
            self.head = node
        else:
            self.tail.prev = node
            node.next = self.tail
        self.tail = node

    def delete(self, node):
        # Node to be deleted is at the beginning
        if node == self.head:
            self.head = self.head.prev
            if self.head is None:
                self.tail = None
            else:
                self.head.next = None
        # Node to be deleted is at the end
        elif node == self.tail:
            self.tail = self.tail.next
            if self.tail is None:
                self.head = None
            else:
                self.tail.prev = None
        # Node to be deleted is in the middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = node.next = None # Clean node references

class LFUCache(object):
    def __init__(self, capacity):
        self.key_to_node = {}
        self.freq_to_ll = defaultdict(DoublyLinkedList)
        self.capacity = capacity
        self.min_freq = 0
        self.cur_size = 0

    def get(self, key):
        '''
        returns value for the passed in key else 1
        Bumps freq on the key's node
        Append node to new freq LinkedList's end
        '''
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.freq_to_ll[node.freq].delete(node)
        if node.freq == self.min_freq and self.freq_to_ll[self.min_freq].head is None:
            self.min_freq += 1
        node.freq += 1
        self.freq_to_ll[node.freq].append(node)
        return node.val

    def put(self, key, val):
        if self.capacity <= 0:
            return
        # Node already present, therefore update frequeny and new value
        # get method updates frequency and places it in new frequency LinkedList,
        # though with the old value, so here we just update node's value
        if self.get(key) != -1:
            self.key_to_node[key].val = val
        else:
            if self.capacity <= self.cur_size: # Threshold reached
                # Delete a node from min freq key
                node_to_delete = self.freq_to_ll[self.min_freq].head
                del self.key_to_node[node_to_delete.key]
                # node_to_delete.prev = node_to_delete.next = None # Clean node references
                self.freq_to_ll[self.min_freq].delete(node_to_delete)
                self.cur_size -= 1
                # this will force it to garbage collect since we removed all
                # references of node_to_delete
            # append current node
            node = DoublyLLNode(key, val)
            self.key_to_node[key] = node
            self.freq_to_ll[node.freq].append(node)
            self.cur_size += 1
            # Whenever you add a node, default back min_freq to 1
            self.min_freq = 1
        
if __name__ == '__main__':
    test_case = (["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
[[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]])
    cache = LFUCache(10)
    for method, arg in zip(test_case[0], test_case[1]):
        print getattr(cache, method)(*arg)
    # test_case = (["put","put","put","put","get","get","get","get","put","get","get","get","get","get"],
    # [[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]])
    # cache = LFUCache(3)
    # for method, arg in zip(test_case[0], test_case[1]):
    #     print getattr(cache, method)(*arg)
    # cache = LFUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print cache.get(1) == 1
    # cache.put(3, 3)
    # print cache.get(2) == -1
    # print cache.get(3) == 3
    # cache.put(4, 4)
    # print cache.get(1) == -1
    # cache.put(3, 3)

    # cache = LFUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print cache.get(1) == 1
    # cache.put(3, 3)
    # print cache.get(2) == -1
    # print cache.get(3) == 3
    # cache.put(4, 4)
    # print cache.get(1) == -1
    # cache.put(3, 3)
    # cache.put(4, 4)
    # # import unittest

    # class Test(unittest.TestCase):
    #     def test_lfu_cache(self):
    #         cache = LFUCache(2)
    #         cache.put(1, 1)
    #         cache.put(2, 2)
    #         self.assertEqual(cache.get(1), 1)
    #         cache.put(3, 3)
    #         self.assertEqual(cache.get(2), -1)
    #         self.assertEqual(cache.get(3), 3)
    #         cache.put(4, 4)
    #         self.assertEqual(cache.get(1), -1)
    #         cache.put(3, 3)
    #         cache.put(4, 4)
    # unittest.main()
