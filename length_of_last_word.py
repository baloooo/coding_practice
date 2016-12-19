"""
Problem statement:

    Given a string s consists of upper/lower-case alphabets and empty space
    characters ' ', return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space
    characters only.

    Example:

    Given s = "Hello World",

    return 5 as length("World") = 5.

    Please make sure you try to solve this problem without using library
    functions. Make sure you only traverse the string once.

"""


def length_of_last_word(target_str):
    length_of_target_str = len(target_str)
    rstrip = False
    count = 0
    while(length_of_target_str):
        length_of_target_str -= 1
        if target_str[length_of_target_str] == ' ':
            if not rstrip:
                continue
            else:
                break
        count += 1
        rstrip = True
    return count


if __name__ == '__main__':
    target_str = '  my name    is    anukul    '
    target_str = 'b '
    print length_of_last_word(target_str)
