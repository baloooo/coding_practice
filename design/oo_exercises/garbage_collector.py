https://en.wikipedia.org/wiki/Tracing_garbage_collection

https://www.geeksforgeeks.org/garbage-collection-python

https://stackoverflow.com/questions/4484167/python-garbage-collector-documentation

Naïve mark-and-sweep:

Naive mark-and-sweep in action on a heap containing eight objects. Arrows represent object references. Circles represent the objects themselves. Objects #1, #2, #3, #4, and #6 are strongly referenced from the root set. On the other hand, objects #5, #7, and #8 are not strongly referenced either directly or indirectly from the root set; therefore, they are garbage.
In the naive mark-and-sweep method, each object in memory has a flag (typically a single bit) reserved for garbage collection use only. This flag is always cleared, except during the collection cycle.

The first stage is the mark stage which does a tree traversal of the entire 'root set' and marks each object that is pointed to by a root as being 'in-use'. All objects that those objects point to, and so on, are marked as well, so that every object that is reachable via the root set is marked.

In the second stage, the sweep stage, all memory is scanned from start to finish, examining all free or used blocks; those not marked as being 'in-use' are not reachable by any roots, and their memory is freed. For objects which were marked in-use, the in-use flag is cleared, preparing for the next cycle.

Tri-color marking:

Three sets are created – white, black and gray:
In many algorithms, initially the black set starts as empty, the gray set is the set of objects which are directly referenced from roots and the white set includes all other objects. Every object in memory is at all times in exactly one of the three sets
The algorithm proceeds as following:

Pick an object from the gray set and move it to the black set.
Move each white object it references to the gray set. This ensures that neither this object nor any object it references can be garbage-collected.
Repeat the last two steps until the gray set is empty.

When the gray set is empty, the scan is complete; the black objects are reachable from the roots, while the white objects are not and can be garbage-collected.

The white set, or condemned set, is the set of objects that are candidates for having their memory recycled.

The black set is the set of objects that can be shown to have no outgoing references to objects in the white set, and to be reachable from the roots. Objects in the black set are not candidates for collection.

The gray set contains all objects reachable from the roots but yet to be scanned for references to "white" objects. Since they are known to be reachable from the roots, they cannot be garbage-collected and will end up in the black set after being scanned.
