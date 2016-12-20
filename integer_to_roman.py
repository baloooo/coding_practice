"""
Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

    Input : 5
    Return : "V"

    Input : 14
    Return : "XIV"
"""

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
    print integer_to_roman(integer_num)
