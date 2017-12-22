"""
Brute force is O(n^3)

Article: https://leetcode.com/articles/longest-valid-parentheses/
"""

class Solution:
    def longestValidParentheses_optimized(self, s):
        """
        Time: O(n) Space: O(1)
        """
        left = right = 0
        maxans = 0
        # Left to right scan
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxans = max(maxans, left+right)
            elif right > left:
                left = right = 0
        # right to left scan
        # for right justified valid strings, right to left scan is needed.
        # Consider the input "(()" , left to right scan will output 0, but the answer is 2.
        left = right = 0
        for c in reversed(s):
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxans = max(maxans, left+right)
            elif left > right: 
                '''
                since we're scanning from R-L, right's will be greater than left consider (()), therefore
                invalid strings are such ()((
                '''
                left = right = 0
        return maxans

    def longestValidParentheses(self, s):
        """
        Time: O(n) space: O(n)
        Article: https://leetcode.com/articles/longest-valid-parentheses/
        """
        maxans, stack = 0, []
        stack.append(-1) # defaults with -1 so as to facilitate length calculation index-(-1) gives the accurate length
        for index, c in enumerate(s):
            if c == '(':
                stack.append(index)
            else:
                stack.pop()
                if len(stack) == 0:
                    '''This also means this was not a match since the only case when sentinel gets popped is when we've
                    encountered mulitple closing parans which are just invalid and the only thing we want from them is to
                    append the last index of those invalid paran to be a sentinel'''
                    stack.append(index)
                else:
                    maxans = max(maxans, index  - stack[-1]) # Notice stack[-1] is not the char that matched (as it's already popped) it's the index before that.
        return maxans

if __name__ == '__main__':
    test_cases = [
        ("()", 2),
        (")()())", 4),
        ("()((()()))())()((()))", 12),
        ("(", 0),
        ("(()", 2),
        ("((((((", 0),
        ("))))))", 0),
        ("()()()(((()()()()", 8),
        ("((()))", 6),
    ]
    for test_case in test_cases:
        res = Solution().longest_valid_paranthesis(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Expected: {1} but got {2}".format(test_case[0], test_case[1], res)  # noqa
