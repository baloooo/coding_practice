'''
Using array: https://leetcode.com/problems/design-circular-queue/discuss/149420/Concise-Java-using-array

'''

class DLLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.k = k
        self.queue_size = 0
        self.head = DLLNode('dummy')
        self.head.next = self.head.prev = self.head


    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.queue_size == self.k:
            return False

        new_node = DLLNode(value)
        # Add new node at end and send it's next to sentinel(head_node)
        new_node.next = self.head
        new_node.prev = self.head.prev # link new_node to previously tail node.

        # Trick here is to now sit at new_node and correct it's prev and next node pointers to point to itself.
        new_node.next.prev = new_node.prev.next = new_node 

        self.queue_size += 1

        return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.queue_size == 0:
            return False

        front_node = self.head.next

        front_node.next.prev = front_node.prev
        front_node.prev.next = front_node.next

        self.queue_size -= 1

        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return self.head.next.value if self.queue_size != 0 else -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return self.head.prev.value if self.queue_size != 0 else -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.queue_size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.queue_size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

##############################################################################################################################
'''
Based on the same concept implementing circular dequeue
'''
class DLLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue_size = 0
        self.k = k
        self.head = DLLNode('dummy')

        self.head.next = self.head.prev = self.head

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.queue_size == self.k:
            return False

        new_node = DLLNode(value)

        new_node.prev = self.head
        new_node.next = self.head.next

        new_node.prev.next = new_node.next.prev = new_node

        self.queue_size += 1

        return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.queue_size == self.k:
            return False

        new_node = DLLNode(value)
        new_node.prev = self.head.prev
        new_node.next = self.head

        new_node.prev.next = new_node.next.prev = new_node

        self.queue_size += 1

        return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.queue_size == 0:
            return False

        front_node = self.head.next

        front_node.prev.next = front_node.next
        front_node.next.prev = front_node.prev

        self.queue_size -= 1

        return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.queue_size == 0:
            return False

        last_node = self.head.prev

        last_node.prev.next = last_node.next
        last_node.next.prev = last_node.prev

        self.queue_size -= 1

        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return self.head.next.value if self.queue_size != 0 else  -1
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return self.head.prev.value if self.queue_size != 0 else  -1
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.queue_size == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.queue_size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
