'''
	Idea: https://leetcode.com/problems/max-stack/solution/
	Time Complexity: O(N) for the popMax operation, and O(1)for the other operations,
			where N is the number of operations performed.

	Space Complexity: O(N), the maximum size of the stack.

        Pop max can be improved by using doublyLL as stack, and a tree map for storing mapping
        of node_val to node_obj in hash map.


'''
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x)) # (ele, cur_max)
        elif x > self.stack[-1][1]:
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.stack[-1][1]))
        

    def pop(self):
        """
        :rtype: int
        """
        try:
            tos = self.stack.pop()
        except IndexError: # Pop from an empty list
            return
        return tos[0]
    
    def top(self):
        """
        :rtype: int
        """
        try:
            return self.stack[-1][0]
        except IndexError:
            pass

    def peekMax(self):
        """
        :rtype: int
        """
        try:
            return self.stack[-1][1]
        except IndexError:
            pass
        

    def popMax(self):
        """
        :rtype: int
        """
        if not self.stack:
            return
        temp_stack = []
        while self.stack:
            tos = self.stack.pop()
            if tos[0] == tos[1]:
                # append back temp_stack in to self.stack, reinstate the next max.
                map(self.push, reversed(temp_stack))
                break
            else:
                temp_stack.append(tos[0])
        return tos[0]
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
