'''
https://leetcode.com/problems/implement-queue-using-stacks/solution/
Idea is to maintain two stacks(i/p and o/p) where we would:
    Always accept new pushes only to i/p stack.
    For the first pop empty entire stack to o/p, and for all successive pop requests pop tos from o/p untill it's empty.
    Trick: Keep a separate variable front which would hold the front of queue when output has not been populated
'''
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []
        self.front = None
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if len(self.input) == 0:
        	self.front = x
        self.input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.output:
        	while self.input:
        		self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.output:
        	return self.output[-1]
        else:
        	return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len((self.input or self.output)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
