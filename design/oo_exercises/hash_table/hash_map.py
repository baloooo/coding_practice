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

A basic requirement is that the function should provide a uniform distribution of hash values. A non-uniform distribution increases the number of collisions and the cost of resolving them. Uniformity is sometimes difficult to ensure by design, but may be evaluated empirically using statistical tests, e.g., a Pearson's chi-squared test for discrete uniform distributions

Load factor = n/k
where n is the number of entries occupied in the hash table & k is the number of buckets.
As the load factor grows larger, the hash table becomes slower, and it may even fail to work (depending on the method used). The expected constant time property of a hash table assumes that the load factor is kept below some bound. For a fixed number of buckets, the time for a lookup grows with the number of entries and therefore the desired constant time is not achieved.

The cost of a table operation is that of scanning the entries of the selected bucket for the desired key. If the distribution of keys is sufficiently uniform, the average cost of a lookup depends only on the average number of keys per bucket—that is, it is roughly proportional to the load factor.

Collision resolution: https://en.wikipedia.org/wiki/Hash_table#Collision_resolution
Separate chaining with linkedlists:
Chained hash tables also inherit the disadvantages of linked lists. When storing small keys and values, the space overhead of the next pointer in each entry record can be significant. An additional disadvantage is that traversing a linked list has poor cache performance, making the processor cache ineffective.

If the load factor is large and some keys are more likely to come up than others, then rearranging the chain with a move-to-front heuristic may be effective. More sophisticated data structures, such as balanced search trees, are worth considering only if the load factor is large (about 10 or more), or if the hash distribution is likely to be very non-uniform, or if one must guarantee good performance even in a worst-case scenario. However, using a larger table and/or a better hash function may be even more effective in those cases

*** Instead of a list, one can use any other data structure that supports the required operations. For example, by using a self-balancing binary search tree, the theoretical worst-case time of common hash table operations (insertion, deletion, lookup) can be brought down to O(log n) rather than O(n).A real world example of a hash table that uses a self-balancing binary search tree for buckets is the HashMap class in Java version 8.

Open addresssing:
    * In another strategy, called open addressing, all entry records are stored in the bucket array itself. When a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found. When searching for an entry, the buckets are scanned in the same sequence, until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table
    * A drawback of all these open addressing schemes is that the number of stored entries cannot exceed the number of slots in the bucket array. In fact, even with good hash functions, their performance dramatically degrades when the load factor grows beyond 0.7 or so. For many applications, these restrictions mandate the use of dynamic resizing, with its attendant costs.
    * Open addressing schemes also put more stringent requirements on the hash function: besides distributing the keys more uniformly over the buckets, the function must also minimize the clustering of hash values that are consecutive in the probe order. Using separate chaining, the only concern is that too many objects map to the same hash value; whether they are adjacent or nearby is completely irrelevant

** Load factor:
    * To keep the load factor under a certain limit, e.g., under 3/4, many table implementations expand the table when items are inserted. For example, in Java's HashMap class the default load factor threshold for table expansion is 3/4 and in Python's dict, table size is resized when load factor is greater than 2/3.
    * Resizing is accompanied by a full or incremental table rehash whereby existing items are mapped to new bucket locations.
    * To limit the proportion of memory wasted due to empty buckets, some implementations also shrink the size of the table—followed by a rehash—when items are deleted. From the point of space–time tradeoffs, this operation is similar to the deallocation in dynamic arrays.
Resizing:
    https://en.wikipedia.org/wiki/Hash_table#Resizing_by_copying_all_entries
When hashtable cannot fit in memory: https://en.wikipedia.org/wiki/Distributed_hash_table
Consistent hashing: https://www.youtube.com/watch?v=--4UgUPCuFM

https://en.wikipedia.org/wiki/Hash_table#Alternativestoall-at-oncerehashing
* Incremental hashing where one makes a new hash table and slowly move existing keys to the new operation.
By keeping in operation both hash tables initially and allowing new entries to go to only on new
hash table, can be a way for expanding hash table size.

* Linear hashing is a dynamic hash table algorithm, it allows for the expansion of the hash table one slot at a time. The frequent single slot expansion can very effectively control the length of the collision chain. The cost of hash table expansion is spread out across each hash table insertion operation, as opposed to being incurred all at once.[2] Linear hashing is therefore well suited for interactive applications. 

* Hashing for distributed hash tables

** Redis cluster is a good example of distributed hash table
Using a hash function like murmurhash can be a good idea.
Using an engineered hash function like Murmur will maximize the quality of the distribution, and minimize the number of collisions, but it offers no other guarantee.
https://stackoverflow.com/questions/11899616/murmurhash-what-is-it

Also in general other points to consider for creating a massive hash table:
    https://stackoverflow.com/questions/7315774/google-interview-question

Code: https://github.com/ishaan007/Data-Structures/blob/master/HashMaps/Map.java
https://github.com/calebmadrigal/algorithms-in-python/blob/master/hashtable.py
https://gist.github.com/kracekumar/91e0d9a250b50ec3c0f3

Things to follow up on:
    Concept and implementation(perhaps): https://en.wikipedia.org/wiki/Consistent_hashing
    Use with distributed hash table
    consistent hashing concept: https://www.youtube.com/watch?v=zaRkONvyGr8
    consistent hashing w/ load balancing GTalk: https://www.youtube.com/watch?v=jk6oiBJxcaA&list=PLwbhGTqjr3LtWxc401hPWh9adQ87--iso&index=7&t=0s

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
        # can be replaced by murmurhash or any other advanced hashing function
        return key % self.size

    def set(self, key, value):
        '''
        If keys are being hashed as in murmur hash we'll store the hash instead of original key.
        '''
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            # Update existing value, if found
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
