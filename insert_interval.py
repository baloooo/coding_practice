

class Solution:
    def __init__(self):
        pass

    def insert_interval(self, intervals, new_interval):
	"""
	Same idea as below just doing it in one pass
        Idea: https://discuss.leetcode.com/topic/17937/two-easy-o-n-c-solutions-with-explanations
	"""
	s, e = newInterval.start, newInterval.end
	left, right = [], []
	for i in intervals:
	    if i.end < s:
		left += i,
	    elif i.start > e:
		right += i,
	    else: # Notice one of them is min and other max
		s = min(s, i.start)
		e = max(e, i.end)
	return left + [Interval(s, e)] + right

    def insert_interval2(self, intervals, new_interval):
		"""
		Best when the initial intervals is already sorted.
        """
        left = [cur_interval for cur_interval in intervals if cur_interval.end < new_interval.start]
        right = [cur_interval for cur_interval in intervals if cur_interval.start > new_interval.end]
        if len(left) + len(right) != len(intervals):
            merge_start = min(new_interval.start, intervals[len(left)].start)
            # since indexing from rear in python starts from index 1 and not zero so we bump it one
            # and as it is rear that means subtract one more
            merge_end = max(new_interval.end, intervals[-len(right)-1].end)
            return left + [Interval(merge_start, merge_end)] + right
        return left + [new_interval] + right

    def insert_interval21(self, intervals, newInterval):
        """
		Same logic as insert_interval2 but included time and space
		efficiencies. But the logic is completely identical
        """
        idx_l = idx_r = 0
        left = []
        right = []
        for idx_l in xrange(len(intervals)):
            if intervals[idx_l].end < newInterval.start:
                left.append(intervals[idx_l])
            else:
                break
        for idx_r in xrange(idx_l, len(intervals)):
            if intervals[idx_r].start > newInterval.end:
                right.append(intervals[idx_r])
        if len(left) + len(right) != len(intervals):
            merge_start = min(newInterval.start, intervals[len(left)].start)
            merge_end = max(newInterval.end, intervals[-len(right)-1].end)
            left.append(Interval(merge_start, merge_end))
            left.extend(right)
            return left
        else:
            # left + [newInterval] + [right]
            left.append(newInterval)
            left.extend(right)
            return left

    def insert_interval3(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        when intervals is not sorted already, we can combine the solution w/ merge interval.
        """
        # using the exact algo as merge interval
        # strategy: Throw the new interval in the intervals list and then sort it
        # on start attribute as we would do for merge_intervals.
        # Now just apply the logic for merge intervals. Mostly everything else should be 
        merged_intervals = []
        intervals.append(newInterval)
        intervals.sort(key=lambda interval: interval.start)
        cur_max_end = intervals[0].end
        merged_intervals = [[intervals[0].start]]
        for interval in intervals[1:]:
            if interval.start > cur_max_end:
                merged_intervals[-1].append(cur_max_end)
                merged_intervals.append([interval.start])
            cur_max_end = max(cur_max_end, interval.end)
        merged_intervals[-1].append(cur_max_end)
        return merged_intervals

if __name__ == '__main__':
    test_cases = [
        (([[1,3],[6,9]], [2, 5]), [[1, 5], [6,9]]),
    ]
    for test_case in test_cases:
        res = Solution().insert_interval(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
