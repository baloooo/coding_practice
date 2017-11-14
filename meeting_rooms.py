'''
Whether you can attend all meetings if intervals are given use

https://discuss.leetcode.com/topic/20959/ac-clean-java-solution
'''

"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] find the minimum number of conference rooms required.
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend(self, arrive, depart):
        # https://discuss.leetcode.com/topic/20959/ac-clean-java-solution
        pass

    def meeting_rooms(self, intervals):
        # list of sorted start intervals
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        # s and e are pointers for starts and ends list respectively
        s = e = 0
        num_rooms = available = 0
        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                if available == 0:
                    num_rooms += 1
                else:
                    available -= 1
                # Increase the pointer as we've accomodated the current request
                s += 1
            else:
                available += 1
                # as one meeting has completed succesfullly
                e += 1
        return num_rooms

    def meeting_rooms_latest(self, intervals):
        """
        @ofLucas explanations is most accurate
        Idea://discuss.leetcode.com/topic/35253/explanation-of-super-easy-java-solution-beats-98-8-from-pinkfloyda
        """
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        rooms = ends_iterator = 0, 0
        for start_time in starts:
            if start_time < ends[ends_iterator]:
                rooms += 1
            else:
                '''
                As when you hit this meeting's end time, you must have surely hit its start time
                as start time < end time and starts and ends are both sorted.
                '''
                ends_iterator += 1
        return rooms

    def meeting_rooms_min_heap(self, intervals):
        """
        Solution using min heap
        Code: https://discuss.leetcode.com/topic/20958/ac-java-solution-using-min-heap/38
        Idea: 
        If you look at these events in a time line one after another (like stream data), then this solution is a greedy solution.

        The heap stores all conflicting events, which must be resolved by independent rooms. The heap's head is the event that has earliest end/finish time. All other events collide with each other mutually in the heap.

        When a new event comes (this is the reason that we need to sort by event.start), we greedily choose the event A that finished the earliest (this is the reason that we use minheap on end time). If the new event does not collide with A, then the new event can re-use A's room, or simply extend A's room to the new event's end time.

        If the new event collides with A, then it must collide with all events in the heap. So a new room must be created.

        The reason for correctness is the invariant: heap size is always the minimum number of rooms we need so far. If the new event collides with everyone, then a new room must be created; if the new event does not collide with someone, then it must not collide with the earliest finish one, so greedily choose that one and re-use that room. So the invariant is maintained.
        """
        from heapq import heappush, heapreplace
        intervals.sort(key=lambda interval: interval.start)
        for interval in intervals:
            print 'start: %s end: %s' % (interval.start, interval.end)
        end_times = [intervals[0]]
        for interval in intervals[1:]:
            # if this meeting starts before the earliest meeting(meeting depicted by top of min heap) ends
            if interval.start < end_times[0].end:
                # we need another room for this meeting
                # heappush(end_times, (interval.end, interval))
                heappush(end_times, interval)
            else:
                # Extend the min interval (Top of heap)
                # heapreplace(end_times(interval.end, interval))
                heapreplace(end_times, interval)
        return len(end_times)

if __name__ == '__main__':
    intervals = [[8, 9], [7, 10]] # 2
    # intervals = [[10,30],[20,50],[5,60]] # 3
    # intervals = [[1, 9], [2,8], [3, 7]] # 3
    arrive = [9, 47, 17, 39, 35, 35, 20, 18, 15, 34, 11, 2, 45, 46, 15, 33, 47, 47, 10, 11, 27]
    depart = [32, 82, 39, 86, 81, 58, 64, 53, 40, 76, 40, 46, 63, 88, 56, 52, 50, 72, 22, 19, 38 ]
    intervals = [Interval(start, end) for start, end in zip(arrive, depart)]
    # intervals = [Interval(start, end) for start, end in intervals]
    test_cases = [
        (intervals, 3),
    ]
    for test_case in test_cases:
        '''
        currently only working sol seems to be first one 'meeting_rooms' method.
        and Easiest to wrap your head around
        '''
        res1 = Solution().meeting_rooms_min_heap(test_case[0])
        res2 = Solution().meeting_rooms(test_case[0])
        print 'res1: %d, res2: %d' %(res1, res2)
        break
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
