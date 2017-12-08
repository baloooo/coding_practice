import collections
import numpy as np

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def max_points(self, points):
        '''
        Bruteforce would be to [calculate slope for all the other points combinations for each point in points]
        Idea: Got the idea here but not sure if/why (dx/dvs, dy/dvs) == slope ? https://discuss.leetcode.com/topic/18447/16ms-28ms-c-solutions-with-explanations/7
        below implementation: https://discuss.leetcode.com/topic/21896/python-68-ms-code/6
        Time: O(n^2)
        Calculate slopes of each point with every other point
        '''
        slopes = collections.defaultdict(int)
        maxp = 0
        for i in xrange(len(points)):
            slopes.clear()
            duplicate = 1
            for j in xrange(i+1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                else:
                    if points[i].x == points[j].x:
                        slope = float('inf')
                    else:
                        '''
                        np(numpy) is used as representation of floating point numbers can be inaccurate
                        therefore rounding off can result in different slopes, so just increasing
                        the purview of slope
                        '''
                        num = ((points[j].y - points[i].y)*np.longdouble(1))
                        denom = (points[j].x - points[i].x)
                        slope = num / denom
                    slopes[slope] += 1
            # max #f points can be point i itself due to large number of duplciates of i
            maxp = max(maxp, duplicate)
            for slope_count in slopes.values():
                # Note: do not forget to add duplicates to slope count at each slope key.
                maxp = max(maxp, slope_count + duplicate)
        return maxp

if __name__ == '__main__':
    test_cases = [
        ([[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]], 6)
    ]
    for test_case in test_cases:
        points = [Point(point[0], point[1]) for point in test_case[0]]
        res = Solution().max_points(points)
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
