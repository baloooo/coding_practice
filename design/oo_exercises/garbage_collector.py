
* In computer programming, tracing garbage collection is a form of automatic memory management that consists of determining which objects should be deallocated ("garbage collected") by tracing which objects are reachable by a chain of references from certain "root" objects

https://en.wikipedia.org/wiki/Tracing_garbage_collection

https://www.geeksforgeeks.org/garbage-collection-python

https://stackoverflow.com/questions/4484167/python-garbage-collector-documentation

Two types of Garbage collection algorithms:

1. Tracing garbage collection:

########################################################################################################
Naïve mark-and-sweep:

Naive mark-and-sweep in action on a heap containing eight objects. Arrows represent object references. Circles represent the objects themselves. Objects #1, #2, #3, #4, and #6 are strongly referenced from the root set. On the other hand, objects #5, #7, and #8 are not strongly referenced either directly or indirectly from the root set; therefore, they are garbage.
In the naive mark-and-sweep method, each object in memory has a flag (typically a single bit) reserved for garbage collection use only. This flag is always cleared, except during the collection cycle.

The first stage is the mark stage which does a tree traversal of the entire 'root set' and marks each object that is pointed to by a root as being 'in-use'. All objects that those objects point to, and so on, are marked as well, so that every object that is reachable via the root set is marked.

In the second stage, the sweep stage, all memory is scanned from start to finish, examining all free or used blocks; those not marked as being 'in-use' are not reachable by any roots, and their memory is freed. For objects which were marked in-use, the in-use flag is cleared, preparing for the next cycle.

########################################################################################################

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

2. Reference counting:
The main advantage of the reference counting over tracing garbage collection is that objects are reclaimed as soon as they can no longer be referenced, and in an incremental fashion, without long pauses for collection cycles and with clearly defined lifetime of every object. In real-time applications or systems with limited memory, this is important to maintain responsiveness. 

Cons:
Although, frequent updates it involves are a source of inefficiency
Also every object should have additional storage for keeping indegree + update them everytime
Cyclic reference detection can be done by some advanced algorithms

Python garbage collection:
Python has a module named "gc" that can be used to create manual garbage collection cycles or initiate one at any time.

Because reference cycles take computational work to discover, garbage collection must be a scheduled activity. Python schedules garbage collection based upon a threshold of object allocations and object deallocations. When the number of allocations minus the number of deallocations are greater than the threshold number, the garbage collector is run.

There are two ways for performing manual garbage collection: time-based and event-based garbage collection.
Time-based garbage collection is simple: the garbage collector is called after a fixed time interval.
Event-based garbage collection calls the garbage collector on event occurrence. For example, when a user exits the application or when the application enters into idle state
