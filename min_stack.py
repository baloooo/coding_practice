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
        if not self.stack:
            # stack is empty therefore directly add
            self.stack.append(x)
            self.min = x
        else:
            # directly add (x-self.min) to the stack
            # This also ensures anytime we have negative number on the stack is
            # when x was less than existing mininum recorded thus far.
            self.stack.append(x-self.min)
            if x < self.min:
                # Update x to new min
                self.min = x

    def pop(self):
        x = self.stack.pop()
        if x < 0:
            """
            if popped element was negative therefore this was the minimum
            element, whose actual value is in self.min but stored value is what
            contributes to get the next min., value stored during push was
            (x - self.old_min) and self.min = x therefore we need to backtrack
            these steps self.min(current) - stack_value(x) actually implies to
                x (self.min) - (x - self.old_min)
            which therefore gives old_min back and therefore can now be set
            back as current self.min.
            """
            self.min = self.min - x

    def top(self):
        x = self.stack[-1]
        if x < 0:
            """
            As discussed above anytime there is a negative value on stack, this
            is the min value so far and therefore actual value is in self.min,
            current stack value is just for getting the next min at the time
            this gets popped.
            """
            return self.min
        else:
            """
            if top element of the stack was positive then it's simple, it was
            not the minimum at the time of pushing it and therefore what we did
            was x(actual) - self.min(min element at current stage) let's say `y`
            therefore we just need to reverse the process to get the actual
            value. Therefore self.min + y, which would translate to
                self.min + x(actual) - self.min, thereby giving x(actual) back
            as desired.
            """
            return x + self.min

    def getMin(self):
        # Always self.min variable holds the minimum so for so easy peezy.
        return self.min


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
    # my_stack = MinStack()
    my_stack = MinStackOptimized()
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
