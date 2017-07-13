"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] find the minimum number of conference rooms required.
"""


class Solution:
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
        num_rooms, available = 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                if available == 0:
                    num_rooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        return num_rooms

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().meeting_rooms(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
