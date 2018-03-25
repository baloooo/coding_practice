"""
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
"""


class Solution:
    def sqrt_optimized(self, x):
        # https://discuss.leetcode.com/topic/8680/a-binary-search-solution/52
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left)/2
            mid_square = mid * mid
            if mid_square == x:
                return mid
            elif mid_square < x:
                left = mid + 1 # since solution can't be mid as we tested above, better to exclude it alogether.
            else:
                right = mid - 1
        # For non perfect squares right will have floor(sqrt(x)) ex for 8, left: 3 right: 2
        # as loop breaked when left went over whereas right went to the floor side of sqrt
        print left, right
        return right


if __name__ == '__main__':
    test_cases = [
        (8, 2),
    ]
    for test_case in test_cases:
        res = Solution().sqrt_optimized(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
