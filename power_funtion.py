"""
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
"""
# Time complexity: O(log(power))

def pow_mod(base, power, mod_no):
    result = 1
    # Update base if it is more than or equal to mod_no
    base = base % mod_no
    while(power > 0):
        if power & 1:
            result = (result * base) % mod_no
        power = power / 2
        base = (base * base) % mod_no
    return result

if __name__ == '__main__':
    base = 2
    power = 5
    mod = 13
    print pow_mod(base, power, mod)
