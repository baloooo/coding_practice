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
def roman_to_integer(s):
    # https://discuss.leetcode.com/topic/17110/my-straightforward-python-solution/5
    roman_map = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    s_val = 0
    for index in xrange(len(s)-1):
        '''
        B'coz of the rule:
	I placed before V or X indicates one less, so four is IV (one less than five) and nine is IX (one less than ten)
	X placed before L or C indicates ten less, so forty is XL (ten less than fifty)
	and ninety is XC (ten less than a hundred)
	C placed before D or M indicates a hundred less, so four hundred is CD 
	(a hundred less than five hundred) and nine hundred is CM (a hundred less than a thousand)
        '''
        if roman_map[s[index]] < roman_map[s[index+1]]:
            s_val -= roman_map[s[index]]
        else:
            s_val += roman_map[s[index]]
    return s_val + roman_map[s[-1]]

if __name__ == '__main__':
    print roman_to_integer('MXL')
