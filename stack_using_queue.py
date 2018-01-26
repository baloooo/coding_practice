'''
https://leetcode.com/problems/implement-stack-using-queues/solution/
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
        cur_size = len(self.q.queue)
        while cur_size > 1:
        	self.q.put(self.q.get())
        	cur_size -= 1

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
