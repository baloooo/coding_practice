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

########################################################################################################

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

########################################################################################################

	def is_valid(self, paran_str, start, end):
        stack = []
        for i in xrange(start, end):
            if paran_str[i] == '(':
                stack.append('(')
            else:
                try:
                    stack.pop()
                except IndexError:
                    return False
        return False if stack else True

    def longestValidParentheses_bruteforce(self, paran_str):
        """
		Good for getting the intution of the exercise.
        """
        max_valid = 0
        for start in xrange(len(paran_str)):
            for end in xrange(start+2, len(paran_str)+1, 2):
                if self.is_valid(paran_str, start, end):
                    max_valid = max(max_valid, end-start)

        return max_valid

########################################################################################################

def longestValidParentheses_dp(self, paran_str):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*len(paran_str)
        max_len = 0

        for i in xrange(1, len(paran_str)):
            if paran_str[i] == ')':
                if paran_str[i-1] == '(':
                    if i >= 2:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                elif (i-dp[i-1] > 0) and paran_str[i-dp[i-1]-1] == '(':
                    if i - dp[i-1] >= 2:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
                max_len = max(max_len, dp[i])
        return max_len

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
