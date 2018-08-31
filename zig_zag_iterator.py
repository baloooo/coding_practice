'''
The current implementation has a unique advantage that we can zigzag iterate over multiple lists not just two with the same
logic.
'''


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        from Queue import Queue
        self.q = Queue()
        # This can be replaced with a loop if given a list of 1d vectors.
        self.q.put(iter(v1))
        self.q.put(iter(v2))
        self.cur_ele = None

    def _get_next_element(self):
        front_ele = None
		# similar to flatten 2d list exercise
        while front_ele is None and self.q.qsize():
            front = self.q.get()
            front_ele = next(front, None)
            if front_ele is not None:
                self.q.put(front)
                break

        self.cur_ele = front_ele

    def next(self):
        """
        :rtype: int
        since you can't tell whether iterator is empty or not without calling next, we'll have to always be a step ahead
        and calculate next_ele
        """
        return self.cur_ele
        

    def hasNext(self):
        """
        :rtype: bool
        """
        self._get_next_element()  # sets the next element to return in self.cur_ele
        return self.cur_ele is not None

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
