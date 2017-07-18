"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        Idea: https://discuss.leetcode.com/topic/15568/detailed-explained-8ms-c-solution
        """
        res = 0
        sign = False
        if dividend < 0 and divisor < 0:
            sign = False
        elif dividend < 0 or divisor < 0:
            sign = True
        dvd = abs(dividend)
        dvs = orig_dvs = abs(divisor)
        while dvd >= orig_dvs:
            quotient = 1
            while dvd >= dvs:
                dvs <<= 1
                quotient <<= 1
            # since loop breaks when they go over limit, so bringing them back in limit
            dvs >>= 1
            quotient >>= 1
            dvd -= dvs
            res += quotient
            dvs = orig_dvs
        res = -res if sign else res
        return min(max(-2147483648, res), 2147483647)
