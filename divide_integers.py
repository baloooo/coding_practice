"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        Time: O(logn) since we exponentially increase divisor from 1 to INT_MAX
        Idea: https://discuss.leetcode.com/topic/15568/detailed-explained-8ms-c-solution
        Main idea is that rather than subtracting divisor one by one from dividend, increase divisor
        exponentially untill it oversteps dividend, recalibrate and repeat the process untill dvd >= dvs.
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
            dvs = orig_dvs

            res += quotient
        res = -res if sign else res
        # return cond'n for overflow can be subsituted by
        #if (!divisor || (dividend == INT_MIN && divisor == -1))
        #            return INT_MAX;
        # or can be written as return min(max(-2147483648, res), 2147483647)
        '''
        this ensures, even if python doesn't overflow on 32 bit integer but this ensures the constraint.
        since 32 bit integers range from -2**31 to 2**31-1, due to one bit used for sign bit
        1. as if our res is less than range of 32 bit int ignore and use min val for 32 bit int.
        2. if our res is more than 2**31-1 use min of res and range for int_max in 32 bit.
        '''
        return min(max(-2**31, res), 2**31-1)
