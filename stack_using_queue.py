'''
Approach3: https://leetcode.com/problems/implement-stack-using-queues/solution/
Idea is to put cur_ele in to queue and then pop all existing elements and push them again, essentially after cur_ele
or can be thought of: pop(get() for Queue) all elements in queue and push cur_ele and then put all elements in again
This ensures queue elements are always in reverse order(stack format)
'''


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
		Push: O(n), rest all methods are O(1)
        """
        from Queue import Queue
        self.q = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)
        for i in xrange(1, self.q.qsize()):
            self.q.put(self.q.get())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
