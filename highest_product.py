"""
Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

Input:

array of integers e.g {1, 2, 3}
 NOTE: Solution will fit in a 32-bit signed integer 
Example:

[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000
"""


class Solution:
    def __init__(self):
        pass

    def highest_product(self, arr):
        if len(arr) <3:
            return None
        max1 = max2 = max3 = -float('inf')
        min1 = min2 = float('inf')
        for ele in arr:
            if ele > max1:
                # Update max, second max, and third max
                max3 = max2
                max2 = max1
                max1 = ele
            elif ele > max2:
                # Update second max and third max
                max3 = max2
                max2 = ele
            elif ele > max3:
                # Update only third max
                max3 = ele
            if ele < min1:
                # Notice this is independent from max if-else since an ele can fall in maxs and mins both
                # Ex: maxes: -5, -4, -1 and mins: -2, -10 with ele as -3
                # Update first and second min
                min2 = min1
                min1 = ele
            elif ele < min2:
                # Update second min
                min2 = ele
        return max(min1*min2*max1, max1*max2*max3)


if __name__ == '__main__':
    test_cases = [
        ([0, -1, 3, 100, 70, 50], 350000),
        ([-10, -10, 1, 3, 2], 300),
        ([ 1, 3, 5, 2, 8, 0, -1, -3 ], 120),
        ([ 81, -95, -22, -86, 67, 31, -28, -64, 25, 47 ], 661770),
        ([1, -4, 3, -6, 7, 0], 168),
        ([-10, -3, -5, -6, -20], -90),
    ]
    for test_case in test_cases:
        res = Solution().highest_product(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
