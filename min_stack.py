# -*- coding: utf-8 -*-
"""
Todo: Complete this using g4g link and extend the same approach for max stack too.


Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.
"""
import sys
'''
Time:  O(n)
Space: O(n) for values + O(1) for bookeeping or should be said as O(1) since space for storing
input from user shouldn't be in extra space used for computation.'''


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

class MinStack2(object):
    '''
    Time: O(n), Space: O(1) as in no extra space apart from storing actual numbers pushed
    Idea: https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

    When element to be inserted is less than minEle, we insert “2x – minEle”.
    The important thing to notes is, 2x – minEle will always be less than x (proved below),
    i.e., new minEle and while popping out this element we will see that something unusual
    has happened as the popped element is less than the minEle. So we will be updating minEle.

        How 2*x - minEle is less than x in push()? 
        x < minEle which means x - minEle < 0

        // Adding x on both sides
        x - minEle + x < 0 + x 

        2*x - minEle < x 

        We can conclude 2*x - minEle < new minEle 
        If we term x as new_min since then only we'll initiate this sequence, we can say:
            pushed_ele = 2*new_min - old_min (1)
        where pushed_ele is the element we'll finally push in to the stack and since from the proof
        above it's clear that this pushed element will be less than min_ele we'll keep track of, while
        popping when we encounter the popped element to be less than min_ele we'll use the same
        relation (1) to get back old_min.
            pushed_ele = 2*new_min - old_min (1)
            old_min = pushed_ele - 2*new_min, where pushed_ele is the element that was pushed and
            is now popped and new_min is the element we termed as minimun back then so the element
            in the self.min variable.
        
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(x)
            self.min = x
        elif x < self.min:
            # pushed_ele = 2*new_min - old_min
            pushed_ele = 2*x - self.min
            self.stack.append(pushed_ele)
            self.min = x
        else:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        pushed_ele = self.stack.pop()
        if pushed_ele < self.min: # A min is being popped, find next min
            self.min = 2*self.min - pushed_ele
            
    def top(self):
        """
        :rtype: int
        """
        tos = self.stack[-1]
        if tos < self.min:
            return self.min
        else:
            return tos
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == '__main__':
    my_stack = MinStack2()
    # my_stack = MinStackOptimized()
    print my_stack.push(2147483646)
    print my_stack.push(2147483646)
    print my_stack.push(2147483647)
    print my_stack.top()
    print my_stack.pop()
    print my_stack.getMin()
    print my_stack.pop()
    print my_stack.getMin()
    print my_stack.pop()
    print my_stack.push(2147483647)
    print my_stack.top()
    print my_stack.getMin()
    print my_stack.push(-2147483648)
    print my_stack.top()
    print my_stack.getMin()
    print my_stack.pop()
    print my_stack.getMin()
    ###3
