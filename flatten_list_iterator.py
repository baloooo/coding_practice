# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
	'''
	Time: O(n) // For traversing it once and once for populating stack.
	Space: O(h) // For stack, where h is the depth of the nested Lists.
	cur implementation: https://discuss.leetcode.com/topic/42042/simple-java-solution-using-a-stack-with-explanation
	Another nice implementation: https://discuss.leetcode.com/topic/41870/real-iterator-in-python-java-c
	Todo: Analyze cur and nice implementaion and if marginal difference move over to other implementation.
	'''

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for i in xrange(len(nestedList), -1, -1):
        	self.stack.append(nestedList[i])
        

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while stack:
        	cur = self.stack[-1]
        	if cur.isInteger():
        		return True
        	else:
        		self.stack.pop()
        		cur_list = cur.getList()
        		for i in xrange(len(cur_list)-1, -1, -1):
        			self.stack.append(cur_list[i])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
