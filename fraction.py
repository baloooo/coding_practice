"""
Fraction
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"
"""


def fraction_as_string(num, denom):
    from collections import OrderedDict
    quot = str(num / denom)
    rem = num % denom
    # {remainder: quotient}
    frac_map = OrderedDict()
    while (rem not in frac_map and rem != 0):
        cur_quot = str((rem*10) / denom)
        frac_map[rem] = cur_quot
        rem = (rem*10) % denom
    if rem == 0 and not frac_map:
        return quot
    count = 0
    quot += '.'
    # import ipdb; ipdb.set_trace()
    for remainder, q in frac_map.items():
        if q != cur_quot:
            count += 1
            quot += q
        else:
            break
    quot += '(' + ''.join(frac_map.values()[count:]) + ')'
    return quot

if __name__ == '__main__':
    # num, denom = 50, 22  # 2.(27)
    # num, denom = 1, 3    # 0.(3)
    # num, denom = 7, 12   # 0.58(3)
    # num, denom = 1, 81   # 0.(012345679)
    num, denom = 22, 7   # 3.(142857)

    print fraction_as_string(num, denom)
