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


class MedianFinder:
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
    def __init__(self):
        self.heaps = [], []

    def add_num(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(small) > len(large):
            heappush(large, -heappop(small))
        print self.heaps

    def find_median(self):
        pass

if __name__ == '__main__':
    m_f_object = MedianFinder()
    m_f_object.add_num(10)
    m_f_object.find_median()
    m_f_object.add_num(20)
    m_f_object.find_median()
    m_f_object.add_num(30)
    m_f_object.find_median()
    m_f_object.add_num(40)
    m_f_object.find_median()
    m_f_object.add_num(5)
    m_f_object.find_median()
    m_f_object.add_num(3)
    m_f_object.find_median()
    m_f_object.add_num(1)
    m_f_object.find_median()
