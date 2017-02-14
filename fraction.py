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
    positive_sign = True
    if num<0:
        positive_sign = not positive_sign
        num = abs(num)
    if denom<0:
        positive_sign = not positive_sign
        denom = abs(denom)
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
    for cur_rem, cur_q in frac_map.items():
        if cur_rem!= rem:
            count += 1
            quot += cur_q
        else:
            break
    if frac_map.values()[count:]:
        quot += '(' + ''.join(frac_map.values()[count:]) + ')'
    if not positive_sign:
        return '-' + quot
    else:
        return quot

if __name__ == '__main__':
    # num, denom = 50, 22  # 2.(27)
    # num, denom = 1, 3    # 0.(3)
    # num, denom = 7, 12   # 0.58(3)
    # num, denom = 1, 81   # 0.(012345679)
    # num, denom = 22, 7   # 3.(142857)
    # num, denom = 2, 1 # 2
    # num, denom = 1, 2 # 0.5
    num, denom = -1, 2 # 0.5

    print fraction_as_string(num, denom)
