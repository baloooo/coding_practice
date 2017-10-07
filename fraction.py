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
import collections

class Solution(object):
    def fractionToDecimal(self, num, denom):
        """
	Time: O(digits in quotient) 
	This solution contains less gotchas and therefore less chances of making silly mistakes. There're lot of
	small things to do in fractionToDecimal2
        """
        # step 1: Get sign
        decimal = []
        if num * denom < 0:
            num = abs(num)
            denom = abs(denom)
            decimal.append('-')
        # This quot now contains the entire quotient before decimal part
        # use divmod as this is faster than doing divide and mod since on assembly level division does return mod
        quot, rem = divmod(num, denom)
        decimal.extend(list(str(quot)))
        if rem == 0:
            return ''.join(decimal)
        decimal.append('.')
        # seen is the mapping of past seen remainders to their index as in when laid out in array
        # so when you encounter a seen remainder you can get the index to carve out the part before it using the index
        seen = {int(rem): len(decimal)}
        while rem != 0:
            rem = rem * 10
            quot, rem = divmod(rem, denom)
            decimal.append(str(quot))
            if rem in seen:
                index = seen[rem]
                decimal =  ''.join(decimal[:index]) + '(' + ''.join(decimal[index:]) + ')'
                break
            seen[rem] = len(decimal)
        return ''.join(decimal)

    def fractionToDecimal2(self, num, denom):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
	Time: O(digits in quotient) 
	Idea: https://discuss.leetcode.com/topic/17071/0ms-c-solution-with-detailed-explanations
        """
	# step 1: Get sign
        decimal = []
	if num * denom < 0:
	    num = abs(num)
	    denom = abs(denom)
            decimal.append('-')
        frac_map = collections.OrderedDict()
        # This quot now contains the entire quotient before decimal part
        quot = list(str(num / denom))
        rem = num % denom
        # This loop will calculate recurring_quot
        # get map of remainder to quotient (stop when remainder repeats)
	# step 2: Populate frac_map to look up remainders
        while rem !=0 and rem not in frac_map:
            re_quot = str((rem*10)/denom)
            frac_map[rem] = re_quot
	    # Note: This is mod for the remainder
            rem = (rem*10) % denom
        # stich together sign, opening and closing braces for recurring digits and so on.
        if sign: decimal.append('-')
	decimal.extend(quot)
	decimal.append('.')
        if rem == 0:
            # proper fraction
            decimal.extend(frac_map.values())
            return ''.join(decimal)

def fraction_as_string(num, denom):
    from collections import OrderedDict
    '''
    Idea: https://discuss.leetcode.com/topic/17071/0ms-c-solution-with-detailed-explanations
    '''
    # Step 1: Check num and denom signs and finalize sign for the end result.
    positive_sign = True
    if num<0:
        positive_sign = not positive_sign
        num = abs(num)
    if denom<0:
        positive_sign = not positive_sign
        denom = abs(denom)
    # step 2 Fill the frac_map and break where recurring remainder encountered
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
    # step 3: Add the recurring part with appropriate '('
    for cur_rem, cur_q in frac_map.items():
        if cur_rem!= rem:
            count += 1
            quot += cur_q
        else:
            opening_brace = False
            for cur_rem, cur_q in frac_map.items():
                if cur_rem != rem:
                    decimal.append(cur_q)
                else:
                    if not opening_brace:
                        decimal.append('(')
			decimal.append(cur_q)
                        opening_brace = True
                    else:
                        break
	decimal.append(')')
        return ''.join(decimal)

if __name__ == '__main__':
    # num, denom = 50, 22  # 2.(27)
    # num, denom = 1, 3    # 0.(3)
    # num, denom = 7, 12   # 0.58(3)
    # num, denom = 1, 81   # 0.(012345679)
    # num, denom = 22, 7   # 3.(142857)
    # num, denom = 2, 1 # 2
    # num, denom = 1, 2 # 0.5
    # num, denom = -1, 2 # 0.5
    # num, denom = 1, 2 # 0.5
    num, denom = 1, 6 # 0.1(6)

    print Solution().fractionToDecimal(num, denom)
