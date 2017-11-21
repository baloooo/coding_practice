"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    def median(self, x, y):
        # This makes sure x is always the smaller array, as we want to B.search on x(convenience)
        if len(x)>len(y):
            self.median(y, x)
        # Notice that end is not on last element but one ahead as we may want to have entire x array on one half
        start, end = 0, len(x)
        one_half = (len(x) + len(y) + 1)/2
        while start <= end: # Binary search on smaller array
            # Fixes the partition pointer for array x
            part_x = (start + end)/2  # this can also be thought as #f element on left half of boundary
            part_y = one_half - part_x # Fixes the partition pointer for array x
            '''
            If partition_x is 0 it means there is nothing on left side, Use -INF for max_left_x
            If partition_x is length of array x then there is nothing on right side, Use +INF for min_right_x
            '''
            max_left_x = x[part_x-1] if part_x != 0 else -float('inf')
            min_right_x = x[part_x] if part_x != len(x) else float('inf')
            max_left_y = y[part_y-1] if part_y != 0 else -float('inf')
            min_right_y = y[part_y] if part_y != len(y) else float('inf')
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                '''
                We found the right places for partitions on x and y
                Now get the max of left elements and min of right elements to get the median in case of
                even length combined arr size or get max of left for odd length combined arr size.
                '''
                if ((len(x) + len(y)) % 2) == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y))/2  # Todo: Why
                else:
                    return max(max_left_x, max_left_y) # Todo: Why
            elif max_left_x > min_right_y: # we're too far on right side for part_x, go left
                end = part_x - 1
            else: # we're too far on left for part_x, go right
                start = part_x + 1



    def find_sorted_median(self, arr1, arr2, median1, median2):
        pass

if __name__ == '__main__':
    test_cases = [
        (([1, 3, 8, 9, 15], [7, 11, 19, 21, 18, 25]), 11),
    ]
    for test_case in test_cases:
        res = Solution().median(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
