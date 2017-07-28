"""
Implement pow(x, n) % d.

In other words, given x, n and d,

find (x^n % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
"""
# Time complexity: O(log(power))


class Solution:
    def __init__(self):
        self.result = 1

    def modulus(self, A, B, C):
        base, power, mod_no = A, B, C

        def power_mod_recursive(base, power, mod_no):
            if power == 0:
                return
            if power % 2 == 1:
                self.result = (self.result * base) % mod_no
            power_mod_recursive((base*base) % mod_no, power/2, mod_no)
        if mod_no == 0:
            return float('inf')
        if power == 0:
            if mod_no == 1:
                return 0
            else:
                return 1
        if base == 0:
            return 0
        base = base % mod_no
        power_mod_recursive(base, power, mod_no)
        return self.result


def pow_mod_iterative(base, power, mod_no):
    if mod_no == 0:
        return float('inf')
    if power == 0:
        if mod_no == 1:
            return 0
        else:
            return 1
    if base == 0:
        return 0
    result = 1
    # Update base if it is more than or equal to mod_no
    base = base % mod_no
    while(power > 0):
        if power & 1:
            result = (result * base) % mod_no
        power = power / 2
        base = (base * base) % mod_no
    return result

class Solution(object):
    """
    https://leetcode.com/problems/powx-n/#/description
    Idea: https://discuss.leetcode.com/topic/40546/iterative-log-n-solution-with-clear-explanation
    """
    def power_function(self, base, power):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        abs_power = abs(power)
        res = 1
        while abs_power >= 1:
            if abs_power & 1:
                res = res * base
            abs_power >>= 1
            base *= base
        if power < 0:
            return 1/res*1.0
        else:
            return res


if __name__ == '__main__':
    # base, power, mod = 2, 5, 13
    # base, power, mod = -1, 1, 20
    base, power, mod = 0, 0, 1
    print pow_mod_iterative(base, power, mod)
    sol = Solution()
    print sol.modulus(base, power, mod)
