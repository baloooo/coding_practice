"""
Problem statement:

    Given an input string, reverse the string word by word.

    Example:

    Given s = "the sky is blue",

    return "blue is sky the".

	    A sequence of non-space characters constitutes a word.
	    Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
	    If there are multiple spaces between words, reduce them to a single space in the reversed string.
"""
import re

def reverse_string(target_string):
	target_string=target_string.strip()    
	target_string_words = re.split('\s+', target_string)
	''.target_string_words[::-1]


if __name__ == '__main__':
    target_string = "the sky is blue"
    print reverse_string(target_string)
