"""
Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

    Input : 5
    Return : "V"

    Input : 14
    Return : "XIV"
"""
def int_roman_optimized(num):
    int_rom_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
        }
    # num = 45266
    sort_keys = sorted(int_rom_map.keys(), reverse=True)
    res = []
    for idx in xrange(len(sort_keys)):
        if sort_keys[idx] <= num:
            freq = num / sort_keys[idx]
            val = int_rom_map[sort_keys[idx]]
            res.append(val*freq)

            num -= (freq * sort_keys[idx])

    return ''.join(res)

def integer_to_roman(num):
    """
    :type num: int
    :rtype: str
    This is better than below solution since this works better for large numbers as 
    this doesn't linearly decrements number. For example for 9964 it would straight
    come down to 964 after first iteration instead of above solution which would take
    9 iteration (in each subtracting 1000) which can easily increase processing time way
    too much.
    """
    int_to_roman_map = {
      1: 'I',
      4: 'IV', # Notice we've intermediate roman values also not only standard ones.
      5: 'V',
      9: 'IX',
      10: 'X',
      40: 'XL',
      50: 'L',
      90: 'XC',
      100: 'C',
      400: 'CD',
      500: 'D',
      900: 'CM',
      1000: 'M'
    }
    num = str(num)
    res = []
    roman_map_keys = sorted(int_to_roman_map.keys(), reverse=True)
    1540 -> 'MDXL'
    for index, digit in enumerate(num):
        cur_digit = int(digit) * (10**(len(num)-1-index))
        for roman_key in roman_map_keys:
            # since roman_keys are reverse sorted the first time we get a roman_key less than our MSB cur_digit, we've got out hit
            if roman_key <= cur_digit: # perfect match

                if cur_digit % roman_key == 0: # For ex: 3000
                    repetition = cur_digit / roman_key
                    res.append(int_to_roman_map[roman_key]*repetition)
                    break
                else: # For ex: 6
                    res.append(int_to_roman_map[roman_key])
                    cur_digit -= roman_key
    return ''.join(res)


int_to_roman_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
}
int_to_roman_map_keys = sorted(int_to_roman_map.keys(), reverse=True)

def integer_to_roman(integer_num):
    roman_number = ''
    for num in int_to_roman_map_keys:
        if not integer_num:
            break
        while(integer_num >= num):
            roman_number += int_to_roman_map[num]
            integer_num -= num
    return roman_number
if __name__ == '__main__':
    integer_num = 1954
    integer_num = 6
    # print integer_to_roman(integer_num)
    print integer_to_roman2(integer_num)
