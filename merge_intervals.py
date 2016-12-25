"""

ven a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        merged_intervals = []
        if not intervals:
            return []
        intervals = sorted(intervals, key = lambda x: x.start)
        interval = intervals[0]
        prev_start = interval.start
        prev_end = interval.end
        for interval in intervals[1:]:
            start = interval.start
            end = interval.end
            if prev_end >= start:
                prev_end = max(prev_end, end) 
                continue
            new_interval = Interval(prev_start, prev_end)
            merged_intervals.append(new_interval)
            prev_start, prev_end = start, end
        final_interval = Interval(prev_start, prev_end)
        merged_intervals.append(final_interval)
        return merged_intervals

