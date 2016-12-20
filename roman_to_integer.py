"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

    Input : "XIV"
    Return : 14
    Input : "XX"
    Output : 20
"""
roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

def roman_to_integer(roman_number):
    num_len = len(roman_number)
    # for index, each in enumerate(roman_number):
    index = integer_number = 0
    while(index<num_len):
        if index < (num_len-1) and (roman_to_int_map[roman_number[index]] < roman_to_int_map[roman_number[index+1]]):
            integer_number += roman_to_int_map[roman_number[index+1]] - roman_to_int_map[roman_number[index]]
            index+=2
        else:
            integer_number += roman_to_int_map[roman_number[index]]
            index+=1
    return integer_number

if __name__ == '__main__':
    roman_number = 'XX'
    roman_number = 'XIV'
    roman_number = 'MCMLIV'
    roman_number = 'MCMXC'
    roman_number = 'MMXIV'
    roman_number = 'V'
    roman_number = ''
    print roman_to_integer(roman_number)
