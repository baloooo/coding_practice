"""
Find the median of the two sorted arrays.

https://www.youtube.com/watch?v=LPFhl65R7ww
https://leetcode.com/articles/median-of-two-sorted-arrays/
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""


class Solution:
    def median(self, x, y):
        '''
        Time: O(log(min(len(x), len(y)))), Space: O(1)
        Broadly saying idea stems from the very definition of median.
        Median divides array in to two parts st.:
            1. len(left_part) = len(right_part)
            2. All elements on LHS of median are <= all elements on RHS
        condition 1 is found using Binary search and condition 2 is tested with max_left_x, ... variables.
        once both conditions are satisfied we note the position of all the variables and depending on
        whether the total no. of items in x and y are even or odd calculate the median.
        '''
        # This makes sure x is always the smaller array, as we want to B.search on x(convenience)
        if len(x)>len(y):
            return self.median(y, x)
        # Notice that end is not on last element but one ahead as we may want to have entire x array on one half
        start, end = 0, len(x)
        first_half = (len(x) + len(y) + 1)/2
        '''
        part_x + part_y = (len(x) + len(y) + 1)/2, where part_x is the #f elements on LHS of array x.
        +1 here is to play nice with both odd and even lengths.
        x=[1,2,4], y = [1,2,3,5] will give you incorrect part_y for part_x 2 if you don't take +1 in
        the above formulae.
        '''
        while start <= end: # Binary search on smaller array
            # Fixes the partition pointer for array x
            part_x = (start + end)/2  # this can also be thought as #f element on left half of boundary
            part_y = first_half - part_x # Fixes the partition pointer for array y
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
                The way we are making partitions makes sure that there are always greater number
                of elements on the LHS of the partition, ie. part_x + part_y >= the #f elements on other half.
                which inturn means for odd length x+y median will always land in max(max_left_x or max_left_y)
                first_half formulae makes sure that first_half is always >= second_half
                '''
                if ((len(x) + len(y)) % 2) == 0:
                    # Ex: a+b+c+d,  max from lefts gives b, mins from right provides c, median (b+c)/2.0
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y))/2.0
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y: # we're too far on right side for part_x, go left
                end = part_x - 1
            else: # we're too far on left for part_x, go right
                start = part_x + 1

if __name__ == '__main__':
    test_cases = [
        # (([1, 3, 8, 9, 15], [7, 11, 19, 21, 18, 25]), 11),
        # (([23, 26, 31, 35], [3, 5, 7, 9, 11, 16]), 13.5),
        # (([10, 15], [5, 20, 30]), 15),
        (([2], []), 2),
    ]
    for test_case in test_cases:
        res = Solution().median(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
