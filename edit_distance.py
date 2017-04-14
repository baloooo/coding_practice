"""
Check if edit distance between two strings is one
An edit between two strings is one of the following changes.

Add a character
Delete a character
Change a character
Given two string s1 and s2, find if s1 can be converted to s2 with exactly one
edit.
Expected time complexity is O(m+n) where m and n are lengths of two strings.
"""


class Solution1:
    def __init__(self):
        pass

    def one_edit_distance(self, str1, str2):
        if abs(len(str1) - len(str2)) > 1:
            return False
        str1_index = str2_index = 0
        edit_distance = 0
        while str1_index < len(str1) and str2_index < len(str2):
            if str1[str1_index] != str2[str2_index]:
                if edit_distance == 1:
                    return False
                if len(str1) > len(str2):
                    # Can be treated as insertion in str2 or deletion at str1
                    str1_index += 1
                elif len(str1) < len(str2):
                    # Can be treated as insertion in str1 or deletion at str2
                    str2_index += 1
                else:
                    # replace char at str1_index and str2_index
                    str1_index += 1
                    str2_index += 1
                edit_distance += 1
            else:
                # replace char at str1_index and str2_index
                str1_index += 1
                str2_index += 1

        return True

"""
Given two words A and B, find the minimum number of steps required to convert A
to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example :
edit distance between
"Anshuman" and "Antihuman" is 2.

    Operation 1: Replace s with t.
    Operation 2: Insert i.
"""


class Solution2:

    def edit_distance(self, str1, str2, str1_index, str2_index):
        if str1_index == len(str1):
            return str2_index
        if str2_index == len(str2):
            return str1_index
        if str1[str1_index] == str2[str2_index]:
            return self.edit_distance(str1, str2, str1_index+1, str2_index+2)
        return 1+min(
            self.edit_distance(str1, str2, str1_index+1, str2_index),
            self.edit_distance(str1, str2, str1_index, str2_index+1),
            self.edit_distance(str1, str2, str1_index+1, str2_index+1)
            )

    def edit_distance(self, str1, str2):
        str1_index = str2_index = 0
        edit_distance_dp = [[0 for _ in xrange(len(str2))]*len(str1)]

if __name__ == '__main__':
    # For finding edit distance
    test_cases = [
        # ('bc', 'c', True),
        # ('abcdefg', 'abcdeab', False),
        # ('aa', 'a', True),
        # ('gfg', 'gf', True),
        ('saturday', 'sunday', 4)
    ]
    for test_case in test_cases:
        res = Solution2().edit_distance(test_case[0], test_case[1], 0, 0)
        if res == test_case[2]:
            print "Passed"
        else:
            print "Failed: Test case: {0},{1} Expected: {2} but got {3}".format(test_case[0], test_case[1], test_case[2], res)  # noqa
    # For one edit distance
    # test_cases = [
    #     ('bc', 'c', True),
    #     ('abcdefg', 'abcdeab', False),
    #     ('aa', 'a', True),
    #     ('gfg', 'gf', True),
    # ]
    # for test_case in test_cases:
    #     res = Solution1().one_edit_distance(test_case[0], test_case[1])
    #     if res == test_case[2]:
    #         print "Passed"
    #     else:
    #         print "Failed: Test case: {0},{1} Expected: {2} but got {3}".format(test_case[0], test_case[1], test_case[2], res)  # noqa
