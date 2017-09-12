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
"""


class HitCounter(object):
    # https://discuss.leetcode.com/topic/48758/super-easy-design-o-1-hit-o-s-gethits-no-fancy-data-structure-is-needed/19

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # q is the hit array
        # each slot in this q/arr is for one second in the 5 minute window
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
        no_of_hits = 0
        for i in xrange(len(self.q)):
            time, hit = self.q[i]
            if timestamp - time < 300:
                no_of_hits += hit
        return no_of_hits

if __name__ == '__main__':
    counter = HitCounter()

    # hit at timestamp 1.
    counter.hit(1)

    # // hit at timestamp 2.
    counter.hit(2)

    # // hit at timestamp 3.
    counter.hit(3)

    # // get hits at timestamp 4, should return 3.
    print counter.getHits(4)

    # // hit at timestamp 300.
    counter.hit(300)

    # // get hits at timestamp 300, should return 4.
    print counter.getHits(300)

    # // get hits at timestamp 301, should return 3.
    print counter.getHits(301)
