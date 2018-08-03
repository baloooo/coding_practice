"""
Note: All operations are done on one string s1(or s2).
Check if edit distance between two strings is one
An edit between two strings is one of the following changes.

Add a character
Delete a character
Change a character
Given two string s1 and s2, find if s1 can be converted to s2 with exactly one
edit.
Expected time complexity is O(m+n) where m and n are lengths of two strings.
One cannot simply replace all the mismatching entries in this scenario since, for strings
x = "abcde"
y = "fabcde"
here instead of replacing each mismatch chars it would be correct to just insert one 'f' at
the beginning and therefore min. edit distance is 1 for x and y.
"""


class Solution1:
    def one_edit_distance_lc(self, s, t):
	'''
	Find if s and t are exact one edit distance apart not more or less.
	'''
	if abs(len(s)-len(t)) > 1: # This is a very nice optimization
	    return False
	one_edit_distance = False
	i = j = 0
	while i < len(s) and j < len(t):
	    if s[i] != t[j]:
		if one_edit_distance:
		    return False
		if len(s) < len(t):
		    j += 1 # consider this an insert on s OR delete on t
		elif len(s) > len(t):
		    i += 1
		else:
		    i += 1
		    j += 1
		one_edit_distance = True
	    else:
		i += 1
		j += 1
	return one_edit_distance or abs(len(s)-len(t)) == 1 # "ab" "abc"

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
                    # Delete in str1
                    str1_index += 1
                elif len(str1) < len(str2):
                    # Insert in str1
                    str2_index += 1
                else:
                    # replace char at str1_index and str2_index
                    str1_index += 1
                    str2_index += 1
                edit_distance += 1
            else:
                # Move both pointers ahead as str1 and str2 are same at current respective indices.
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

    def get_min_distance_recursion_old(self, w1, w2, idx1, idx2):
        # Time: O(3^m)
        # Space: O(stack depth) which is O(max(len(str1), len(str2)))
        # recursion from tail without wonky + 2 on line 96 here
        if idx1 == 0:
            return idx2
        if idx2 == 0:
            return idx1
        if w1[idx1-1] == w2[idx2-1]:
            return self.get_min_distance(w1, w2, idx1 - 1, idx2 - 1)
        return 1 + min(
                self.get_min_distance(w1, w2, idx1 - 1, idx2),
                self.get_min_distance(w1, w2, idx1, idx2 - 1),
                self.get_min_distance(w1, w2, idx1 - 1, idx2 - 1)
            )

    def edit_distance_recursion_new(self, str1, str2, str1_index, str2_index):
        """
        Time: O(3^m)
        Space: O(stack depth) which is O(max(len(str1), len(str2)))
        Traverse from tail since this will save you some computations on returning lengths etc
        """
        if str1_index == len(str1):
            return len(str2)-str2_index
        if str2_index == len(str2):
            return len(str1)-str1_index
        if str1[str1_index] == str2[str2_index]:
            return self.edit_distance(str1, str2, str1_index+1, str2_index + 1)
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
        Todo: Complete the 1D version from below link.
        https://discuss.leetcode.com/topic/17639/20ms-detailed-explained-c-solutions-o-n-space
        https://www.youtube.com/watch?v=b6AGUjqIPsA    # his insert and delete representations
        are accurate and intutive when chalked graphically, start by constructing a 2d array
        and naming rows and cols as shown in the video, helps make a better image of the sol'n
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
        # ('saturday', 'sunday', 3)
        ('teacher', 'tache', False)
    ]
    for test_case in test_cases:
        # res = Solution2().edit_distance_dp(test_case[0], test_case[1], 0, 0)
        # res = Solution2().edit_distance_dp(test_case[0], test_case[1])
        res = Solution1().one_edit_distance_lc(test_case[0], test_case[1])
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
