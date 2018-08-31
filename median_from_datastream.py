"""
Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data
structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
from heapq import heappush, heappop, heappushpop


"""
Heap snapshot for input:
    ([], [10])
    ([-10], [20])
    ([-10], [20, 30])
    ([-20, -10], [30, 40])
    ([-10, -5], [20, 40, 30])
    ([-10, -5, -3], [20, 40, 30])
    ([-5, -1, -3], [10, 20, 30, 40])
"""
class MedianFinder(object):
    """
    Idea: https://discuss.leetcode.com/topic/27522/java-python-two-heap-solution-o-log-n-add-o-1-find
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_max_heap, self.large_min_heap = [], []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # Note: Adding element to any of the heaps require element come from other heap so as to preserve the sorted
        # sequence property
        if len(self.small_max_heap) == len(self.large_min_heap):
            # push in large
            # negate element before putting in min_heap and since finally putting in to max heap, 
            # so bring it back to original value
            heapq.heappush(self.large_min_heap, -heapq.heappushpop(self.small_max_heap, -num))
        else:
            # put actual number in as initially putting to min_heap which is auto-implemented in python
            # but while putting in to max_heap negate the number so as to preserve overall max_heap property.
            heapq.heappush(self.small_max_heap, -heapq.heappushpop(self.large_min_heap, num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small_max_heap) == len(self.large_min_heap):
            #return (self.small_max_heap[0] + self.large_min_heap[0])/2.0
            # Since elements in self.large are negated so, negate them again to get a+b/2.0
            return (self.large_min_heap[0] - self.small_max_heap[0])/2.0
        else:
            return self.large_min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == '__main__':
    m_f_object = MedianFinder()
    m_f_object.add_num(10)
    print m_f_object.find_median()
    m_f_object.add_num(20)
    print m_f_object.find_median()
    m_f_object.add_num(30)
    print m_f_object.find_median()
    m_f_object.add_num(40)
    print m_f_object.find_median()
    m_f_object.add_num(5)
    print m_f_object.find_median()
    m_f_object.add_num(3)
    print m_f_object.find_median()
    m_f_object.add_num(1)
    print m_f_object.find_median()
