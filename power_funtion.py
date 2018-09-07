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
        '''
        Preferable than above since it is iterative
        Idea is similar to power_function below
        check out these, if you need some revision on mod rules
        https://math.stackexchange.com/questions/111330/explain-for-students-why-does-0-mod-n-equal-0-zero
        https://math.stackexchange.com/questions/516251/why-is-n-mod-0-undefined
        '''
        # check if any of the three are zero
        if mod_no == 0:
            return float('inf') # b'coz a % 0 is always infinite
        if power == 0:
            if mod_no == 1:
                return 0 # b'coz 1 mod 1 is zero
            else:
                return 1 # b'coz 1 mod x is always 1
        if base == 0:
            return 0 # b'coz 0 mod x is always 0
        result = 1
        # Update base if it is more than or equal to mod_no
        base = base % mod_no
        while(power > 0):
            if power & 1:
                result = (result * base) % mod_no
            power = power / 2
            base = (base * base) % mod_no
        return result

    def b_mul(self, base, power):
        if power == 0:
            return 1
        half = self.b_mul(base, power/2)
        if power % 2 == 0:
            return half * half
        else:
            return base * half * half

    def power_function_alternate(self, base, power):
        """
        :type x: float
        :type n: int
        :rtype: float
        Idea is that if we know (base)^(n/2) we can just double it to get base ^ n, so we initially find 
		Same as below but more intutive, although due to recursion takes O(logn) space too
        """
        res = self.b_mul(base, abs(power))
        if power < 1:
            return 1/(res*1.0)
        else:
            return res


    def power_function(self, base, power):
        """
        https://leetcode.com/problems/powx-n/#/description
        The idea is to make only logn operations for getting the power(x, n) instead of O(n),
        which can be got if we do operations on cue from binary representation of power.
        Idea: https://discuss.leetcode.com/topic/40546/iterative-log-n-solution-with-clear-explanation
			N = 9 = 2^3 + 2^0 = 1001 in binary. Then:

			x^9 = x^(2^3) * x^(2^0)

			We can see that every time we encounter a 1 in the binary representation of N, we need to multiply
			the answer with x^(2^i) where i is the ith bit of the exponent. Thus, we can keep a running total
			of repeatedly squaring x - (x, x^2, x^4, x^8, etc) and multiply it by the answer when we see a 1.

			To handle the case where N=INTEGER_MIN we use a long (64-bit) variable. Below is solution:
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
