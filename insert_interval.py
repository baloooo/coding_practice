

class Solution:
    def __init__(self):
        pass

    def insert_interval(self, intervals, new_interval):
	"""
	Same idea as below just doing it in one pass
	"""
	s, e = newInterval.start, newInterval.end
	left, right = [], []
	for i in intervals:
	    if i.end < s:
		left += i,
	    elif i.start > e:
		right += i,
	    else:
		s = min(s, i.start)
		e = max(e, i.end)
	return left + [Interval(s, e)] + right

    def insert_interval(self, intervals, new_interval):
	"""
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left = [cur_interval for cur_interval in intervals if cur_interval.end < new_interval.start]
        right = [cur_interval for cur_interval in intervals if cur_interval.start > new_interval.end]
        if len(left) + len(right) != len(intervals):
            merge_start = min(new_interval.start, intervals[len(left)].start)
            merge_end = max(new_interval.end, intervals[-len(right)-1].end)
            return left + [Interval(merge_start, merge_end)] + right
        return left + [new_interval] + right

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
