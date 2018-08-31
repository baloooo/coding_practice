"""
Design a hit counter which counts the number of hits received in the past 5
minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you
may assume that calls are being made to the system in chronological order
(ie, the timestamp is monotonically increasing). You may assume that the
earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);

Possible solutions:
https://discuss.leetcode.com/topic/48758/super-easy-design-o-1-hit-o-s-gethits-no-fancy-data-structure-is-needed
http://massivetechinterview.blogspot.jp/2015/06/algorithm-how-to-count-number-of.html
https://stackoverflow.com/questions/17562089/how-to-count-number-of-requests-in-last-second-minute-and-hour

scalable strategy:
https://leetcode.com/problems/design-hit-counter/discuss/83510/AC-scalable-0ms-super-easy-C++-design-with-queue-and-aggregated-O(1)-operation-for-hit-and-gethits
Another strategy would be to use a queue for storing hits and for every hit remove all timestamps from head of queue that
occurred before the current 300 ms timestamp(while removing a timestamp decrement its count from running count of hits)
Similarly on getHits call remove all hits from head of queue that happened earlier than 300ms window and return current running
count of the hits.

Pros:
    No array size dependency on hitcounter window, as a global variable can change that and queue will start clearing or 
    adding hits in to queue with the new window. This cannot be done in current implementation as size is fixed in init
    and we only add hits with indexes afterwards.
"""


class HitCounter(object):
    # https://discuss.leetcode.com/topic/48758/super-easy-design-o-1-hit-o-s-gethits-no-fancy-data-structure-is-needed/19

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # q is the hit array
        # each slot in this q/arr is for one second in the 5 minute window
		# The idea is to have 300 slots each for every second(since exercise restricts time granularity to seconds).
        self.q = [(0, 0) for _ in xrange(300)]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        idx = timestamp % 300
        time, hit = self.q[idx]
        if time != timestamp:
            self.q[idx] = timestamp, 1
        else:
            self.q[idx] = time, hit + 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
		count = 0
		for ts, hits in self.hit_cache:
			if (timestamp - ts) < 300:
				count += hits
		return count
