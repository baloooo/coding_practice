'''
Source:
https://www.geeksforgeeks.org/implementing-our-own-hash-table-with-separate-chaining-in-java/
https://en.wikipedia.org/wiki/Hash_table
https://stackoverflow.com/questions/9364134/what-hashing-function-does-java-use-to-implement-hashtable-class
https://stackoverflow.com/questions/793761/built-in-python-hash-function?noredirect=1&lq=1

Often this is done in two steps:

hash = hashfunc(key)
index = hash % array_size
In this method, the hash is independent of the array size, and it is then reduced to an index (a number between 0 and array_size − 1) using the modulo operator (%).

In the case that the array size is a power of two, the remainder operation is reduced to masking, which improves speed, but can increase problems with a poor hash function.

A basic requirement is that the function should provide a uniform distribution of hash values. A non-uniform distribution increases the number of collisions and the cost of resolving them. Uniformity is sometimes difficult to ensure by design, but may be evaluated empirically using statistical tests, e.g., a Pearson's chi-squared test for discrete uniform distributions

Load factor = n/k
where n is the number of entries occupied in the hash table & k is the number of buckets.
As the load factor grows larger, the hash table becomes slower, and it may even fail to work (depending on the method used). The expected constant time property of a hash table assumes that the load factor is kept below some bound. For a fixed number of buckets, the time for a lookup grows with the number of entries and therefore the desired constant time is not achieved.

Collision resolution: https://en.wikipedia.org/wiki/Hash_table#Collision_resolution
Separate chaining with linkedlists:
For this reason, chained hash tables remain effective even when the number of table entries n is much higher than the number of slots. For example, a chained hash table with 1000 slots and 10,000 stored keys (load factor 10) is five to ten times slower than a 10,000-slot table (load factor 1); but still 1000 times faster than a plain sequential list.
Chained hash tables also inherit the disadvantages of linked lists. When storing small keys and values, the space overhead of the next pointer in each entry record can be significant. An additional disadvantage is that traversing a linked list has poor cache performance, making the processor cache ineffective.

Open addresssing:
    * In another strategy, called open addressing, all entry records are stored in the bucket array itself. When a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found. When searching for an entry, the buckets are scanned in the same sequence, until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table
    * A drawback of all these open addressing schemes is that the number of stored entries cannot exceed the number of slots in the bucket array. In fact, even with good hash functions, their performance dramatically degrades when the load factor grows beyond 0.7 or so. For many applications, these restrictions mandate the use of dynamic resizing, with its attendant costs.
    * Open addressing schemes also put more stringent requirements on the hash function: besides distributing the keys more uniformly over the buckets, the function must also minimize the clustering of hash values that are consecutive in the probe order. Using separate chaining, the only concern is that too many objects map to the same hash value; whether they are adjacent or nearby is completely irrelevant
Load factor:
    * To keep the load factor under a certain limit, e.g., under 3/4, many table implementations expand the table when items are inserted. For example, in Java's HashMap class the default load factor threshold for table expansion is 3/4 and in Python's dict, table size is resized when load factor is greater than 2/3.
    * Resizing is accompanied by a full or incremental table rehash whereby existing items are mapped to new bucket locations.
    * To limit the proportion of memory wasted due to empty buckets, some implementations also shrink the size of the table—followed by a rehash—when items are deleted. From the point of space–time tradeoffs, this operation is similar to the deallocation in dynamic arrays.
Resizing:
    https://en.wikipedia.org/wiki/Hash_table#Resizing_by_copying_all_entries
When hashtable cannot fit in memory: https://en.wikipedia.org/wiki/Distributed_hash_table
Consistent hashing: https://www.youtube.com/watch?v=--4UgUPCuFM

Java does in its own implementation of Hash Table uses Binary Search Tree if linked list corresponding to a particular bucket tend to get too long.

Code: https://github.com/ishaan007/Data-Structures/blob/master/HashMaps/Map.java
https://github.com/calebmadrigal/algorithms-in-python/blob/master/hashtable.py
https://gist.github.com/kracekumar/91e0d9a250b50ec3c0f3
'''

class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Key not found')
