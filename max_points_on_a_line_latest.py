# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
import collections


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)
        point_count_map = {}
        temp = []
        for point in points:
            cur_point = (point.x, point.y)
            if cur_point in point_count_map:
                point_count_map[cur_point] += 1
            else:
                point_count_map[cur_point] = 1
                temp.append(point)
        points = temp
        slope_points_map = collections.defaultdict(list)
        for i in xrange(len(points)):
            base_point = points[i]
            for j in xrange(i+1, len(points)):
                cur_point = points[j]
                cur_slope = float('inf')
                if cur_point.x-base_point.x != 0:
                    cur_slope = abs((cur_point.y - base_point.y)/(cur_point.x-base_point.x)*1.0)
                slope_points_map[cur_slope].append(base_point)
                import ipdb; ipdb.set_trace()
        max_count = 0
        import ipdb; ipdb.set_trace()
        for same_slope_points in slope_points_map.values():
            cur_count = 0
            for each in same_slope_points:
                cur_point = (each.x, each.y)
                if cur_point in point_count_map:
                    cur_count += point_count_map[cur_point]
                else:
                    cur_count += 1
            max_count = max(max_count, cur_count)
        return max_count

if __name__ == '__main__':
    points = [[0,0],[0,0]]
    temp = []
    for point in points:
        temp.append(Point(point[0], point[1]))
    points = temp
    print Solution().maxPoints(points)
