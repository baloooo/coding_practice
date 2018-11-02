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

class NestedIterator_naive(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # tmp storage for next element, when initializing we move the first element into it.
        self.stack = [iter(nestedList)] # Make an iterator over original list
        self.next_element = None
		# This next call sets up the base layer and initializes self.next_element
        self.next()
        

    def next(self):
        """
        :rtype: int
        self.next_element is set when all required iterators are correctly set, and we are ready to fetch element from iterators.
        If element under cur_iterator is a list, create a new iterator for it and populate next_element from it
        else set next_element and return
        """
        if self.next_element is not None:
			'''
			Now after that whenever next() is called by user next_element is used and returned and a call to next() is made
			from within so as to initialize it for the next call
			'''
            return_val = self.next_element
            self.next_element = None
            self.next()
            return return_val
        
        cur_ele = None
        while self.stack and cur_ele is None:
            cur_ele = next(self.stack[-1], None)
            if cur_ele is None:
                self.stack.pop()

        
        # if stack is empty return
        if cur_ele is None:
            return
        
        if cur_ele.isInteger():
            self.next_element = cur_ele.getInteger()
        else:
            self.stack.append(iter(cur_ele.getList()))
            self.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_element is not None

##############################################################################################################################

class NestedIterator_optimized(object):
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

# if __name__ == '__main__':
# 	my_list =  [[1,1],2,[1,1]]
# 	for each in my_list:
# 		if isinstance(each, list):
# 			inside_list = []
# 			for ele in each:
# 				inside_list.append(NestedInteger(
# 			nestedList.append(NestedInteger
# 	nestedList = []
# 	# Your NestedIterator object will be instantiated and called as such:
# 	i, v = NestedIterator(nestedList), []
# 	while i.hasNext(): v.append(i.next())
