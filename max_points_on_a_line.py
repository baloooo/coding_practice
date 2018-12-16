# coding: utf-8

import collections
import numpy as np

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def max_points_optimized(self, points):
        '''
        https://www.geeksforgeeks.org/count-maximum-points-on-same-line/
        Idea:
            Main idea is to calculate slope for each combination of points in the list.
            and check which slope as the maximum number of points on it.

            Gotchas: Deal with duplicate points.
            Deal with points on x-axis and y-axis.

            If two point are (x1, y1) and (x2, y2) then their slope will be
            (y2 – y1) / (x2 – x1) which can be a double value and can cause precision
            problems. To get rid of the precision problems, we treat slope as pair
            ((y2 – y1), (x2 – x1)) instead of ratio and reduce pair by their gcd before
            inserting into map. In below code points which are vertical or repeated are
            treated separately.
        '''
        from fractions import gcd
        if len(points) <= 1: return len(points)
        slopes = collections.defaultdict(int)
        maxp = 0
        for i in xrange(len(points)):
            overlapping_points = cur_max = 0
            base_point = points[i]

            for j in xrange(i+1, len(points)):
                cur_point = points[j]
                # check if duplicate points
                if base_point.x == cur_point.x and base_point.y == cur_point.y:
                    overlapping_points += 1
                else:
                    ydiff = cur_point.y - base_point.y
                    xdiff = cur_point.x - base_point.x

                    g = gcd(xdiff, ydiff)
                    ydiff = ydiff/g
                    xdiff = xdiff/g

                    slopes[(ydiff, xdiff)] += 1

                    cur_max = max(cur_max, slopes[(ydiff, xdiff)])
            # total points are whatever maximum we've found till now
            # + overlapping points for the base point + base point itself.
            # since cur_max is the maximum points in line with base_point, and since overlapping points
            # are points same as base_point we can add that and then 1 for the base point itself.
            maxp = max(maxp, cur_max + overlapping_points + 1)
            slopes.clear()  # Note: we need to clear the slopes after every base point covered.
        return maxp


    def max_points(self, points):
        '''
        Bruteforce would be to [calculate slope for all the other points combinations for each point in points]
		and then iterate over all of them each time to check if slope exists. Time complexity would be O(n^3) as for each O(n^2) iteration we would go over all the n points slopes to check match.

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
