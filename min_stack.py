# -*- coding: utf-8 -*-
"""
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.
"""
import sys

# Time:  O(n)
# Space: O(1)


class MinStackOptimized:
    def __init__(self):
        self.stack = []
        self.min = sys.maxint

    def push(self, x):
        if x < self.min:
            self.stack.append((x, x))
            self.min = x
        else:
            self.stack.append((x, self.min))

    def pop(self):
        try:
            self.stack.pop()
        except IndexError:
            # can implement any custom behavior for pop on empty stack
            pass

    def top(self):
        try:
            return self.stack[-1][0]
        except IndexError:
            # can implement any custom behavior for top on empty stack
            pass

    def getMin(self):
        try:
            return self.stack[-1][1]
        except IndexError:
            # can implement any custom behavior for getMin on empty stack
            pass


# Time:  O(n)
# Space: O(n)


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if (not self.stack) or (x < self.stack[-1][1]):
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.stack[-1][1]))
        # if x < self.min:
        #     self.stack.append((x, x))
        #     self.min = x
        # else:
        #     self.stack.append((x, self.min))

    def pop(self):
        try:
            self.stack.pop()
        except IndexError:
            # can implement any custom behavior for pop on empty stack
            pass

    def top(self):
        try:
            return self.stack[-1][0]
        except IndexError:
            # can implement any custom behavior for top on empty stack
            return -1

    def getMin(self):
        try:
            return self.stack[-1][1]
        except IndexError:
            # can implement any custom behavior for getMin on empty stack
            return -1

if __name__ == '__main__':
    my_stack = MinStack()
    # my_stack = MinStackOptimized()
    my_stack.push(780809279)
    my_stack.getMin()
    my_stack.push(57337424)
    my_stack.push(998849637)
    my_stack.top()
    my_stack.pop()
    my_stack.push(514381243)
    my_stack.pop()
    my_stack.top()
    my_stack.top()
    my_stack.pop()
    my_stack.top()
    my_stack.push(814651044)
    print my_stack.getMin()
