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

    def edit_distance_recursion(self, str1, str2, str1_index, str2_index):
        """
        Time: O(3^m)
        Space: O(stack depth) which is O(max(len(str1), len(str2)))
        """
        if str1_index == len(str1):
            return len(str2)-str2_index
        if str2_index == len(str2):
            return len(str1)-str1_index
        if str1[str1_index] == str2[str2_index]:
            return self.edit_distance(str1, str2, str1_index+1, str2_index+2)
        # else:
        return 1+min(
            self.edit_distance(str1, str2, str1_index+1, str2_index),  # noqa Insert/Delete in str2
            self.edit_distance(str1, str2, str1_index, str2_index+1),  # noqa Insert/Delete in str1
            self.edit_distance(str1, str2, str1_index+1, str2_index+1)  # noqa Replace
            )

    def edit_distance_dp(self, str1, str2):
        """
        Time: O(m*n)
        Space: O(m*n)
        http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
        https://discuss.leetcode.com/topic/17639/20ms-detailed-explained-c-solutions-o-n-space
        https://www.youtube.com/watch?v=b6AGUjqIPsA
        """
        dp = [[0 for _ in xrange(len(str2)+1)] for _ in xrange(len(str1)+1)]
        for i in xrange(len(str1)+1):
            for j in xrange(len(str2)+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1])
        return dp[len(str1)][len(str2)]

if __name__ == '__main__':
    # For finding edit distance
    test_cases = [
        # ('bc', 'c', True),
        # ('abcdefg', 'abcdeab', False),
        # ('aa', 'a', True),
        # ('gfg', 'gf', True),
        ('saturday', 'sunday', 3)
    ]
    for test_case in test_cases:
        # res = Solution2().edit_distance_dp(test_case[0], test_case[1], 0, 0)
        res = Solution2().edit_distance_dp(test_case[0], test_case[1])
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
