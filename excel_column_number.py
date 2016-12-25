"""
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1
    
    B -> 2
    
    C -> 3
    
    ...
    
    Z -> 26
    
    AA -> 27
    
    AB -> 28 
"""
import string
def column_title_to_number(title):
    title_to_number_map = {}
    column_number = 0
    for key, val in zip(list(string.ascii_uppercase), range(1, 27)):
        title_to_number_map[key] = val
    title_len = len(title) - 1
    power = 0
    while(title_len>=0):
        column_number += (26**power)*title_to_number_map[title[title_len]]
        power+=1
        title_len-=1
    return column_number

if __name__ == '__main__':
    print column_title_to_number('ZZ')
