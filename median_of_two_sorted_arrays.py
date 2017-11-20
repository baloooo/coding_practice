"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    def __init__(self):
        pass

    def median(self, arr):
        pass

    def find_sorted_median(self, arr1, arr2, median1, median2):
        https://www.youtube.com/watch?v=LPFhl65R7ww
        https://leetcode.com/articles/median-of-two-sorted-arrays/
        https://leetcode.com/problems/median-of-two-sorted-arrays/description/
        pass

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
