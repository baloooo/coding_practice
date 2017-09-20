"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def __init__(self):
        pass

    def my_func(self, arr, target):
        import sys
	arr.sort()
        closest = sys.maxint
        for index in xrange(len(arr)-2):
            start, end = index + 1, len(arr)-1
            while start < end:
                cur_closest = arr[index] + arr[start] + arr[end]
                if cur_closest == target:
                    return target
                elif cur_closest < target:
                    start += 1
                else:
                    end -= 1
                if abs(target-closest) > abs(target-cur_closest):
                    closest = cur_closest
        return closest

if __name__ == '__main__':
    test_cases = [
        (([-1, 2, 1, -4], 1), 2),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
