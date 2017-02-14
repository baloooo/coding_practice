class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        arr_x = A
        arr_y = B
        #print A
        #print B
        if len(arr_x) == 0:
            return 0
        if len(arr_x) == 1:
            return 1
        if len(arr_y) == 2:
            return 2
        import sys
        # {(point, slope): count}
        slope_count_map = {}
        total_pairs = []
        max_slope_count = 0
        # get total number of points
        for index in range(len(arr_x)-1):
            cur_x, cur_y = arr_x[index], arr_y[index]
            for (x,y) in zip(arr_x[index+1:], arr_y[index+1:]):
                total_pairs.append(((cur_x, cur_y), (x, y)))
        for cur_pair in total_pairs:
            first_point = cur_pair[0] # (x1, y1)
            second_point = cur_pair[1]# (x2, y2)
            # handle points on vertical line, therefore undefined slope.
            if (second_point[0] - first_point[0]) == 0:
                cur_slope = sys.maxsize
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
