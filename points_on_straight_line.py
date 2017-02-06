"""
Points on the Straight Line
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :

(1, 1)
(2, 2)
Sample Output :

2
You will be give 2 arrays X and Y. Each point is represented by (X[i], Y[i])
"""
from __future__ import division

def max_points_in_st_line(arr_x, arr_y):
    import sys
    # {(point, slope): count}
    if len(arr_x) == 0:
        return 0
    if len(arr_x) == 1:
        return 1
    if len(arr_x) == 2:
        return 2
    slope_count_map = {}
    total_pairs = []
    max_slope_count = 0
    # get total number of points
    for index in xrange(len(arr_x)-1):
        cur_x, cur_y = arr_x[index], arr_y[index]
        for (x,y) in zip(arr_x[index+1:], arr_y[index+1:]):
            total_pairs.append(((cur_x, cur_y), (x, y)))
    for cur_pair in total_pairs:
        first_point = cur_pair[0] # (x1, y1)
        second_point = cur_pair[1]# (x2, y2)
        # handle points on vertical line, therefore undefined slope.
        if (second_point[0] - first_point[0]) == 0:
            cur_slope = sys.maxint
        else:
            cur_slope = (second_point[1] - first_point[1]) / (second_point[0] - first_point[0])*1.0
        slope_count_map[cur_slope] = 2
        orig_pair_traversed = False
        count = 0
        for (x,y) in zip(arr_x, arr_y):
            temp_slope = sys.maxint
            if (first_point[0] - x) != 0:
                temp_slope = abs((first_point[1] - y) / (first_point[0] - x))*1.0
            if (x,y) in cur_pair:
                if not orig_pair_traversed:
                    if count == 0:
                        count += 1
                    else:
                        orig_pair_traversed = True
                    continue
            if abs(cur_slope) == temp_slope:
                # print 'Adding cur_pair %s and new_pair %s' % (cur_pair, (x,y))
                slope_count_map[cur_slope] += 1
        cur_max_slope_count = max(slope_count_map.values())
        if cur_max_slope_count > max_slope_count:
            max_slope_count = cur_max_slope_count
        # print slope_count_map
        slope_count_map =  {}
    return max_slope_count

if __name__ == '__main__':
    # arr_x = [1, 2]
    # arr_y = [1, 2]
    arr_x = [1, 2, 3, 4, -8]
    arr_y = [0, 1, 2, 4, -8]
    arr_x = [1, 1, 1]
    arr_y = [0, 4, -1]
    arr_x = [1, 1, 1, 1, 1]
    arr_y = [1, 1, 1, 1, 1]
    # arr_x = [-6, -17, 5, -16, -18, -17]
    # arr_y = [2, -4, 5, -13, -2, 20]
    arr_x = [-6, 5, -18, 2, 5, -2]
    arr_y = [-17, -16, -17, -4, -13, 20]
    # -6 -17 5 -16 -18 -17 2 -4 5 -13 -2 20
    print max_points_in_st_line(arr_x, arr_y)
